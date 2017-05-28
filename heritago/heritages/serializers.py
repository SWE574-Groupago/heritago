import django.dispatch
from rest_framework import serializers

from heritages.models import Heritage, BasicInformation, Origin, Tag, Multimedia, Selector, AnnotationTarget, \
    AnnotationBody, Annotation, User


class BasicInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicInformation
        fields = ("name",
                  "value")


class OriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origin
        fields = ("name",)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name",)


class MultimediaSerializer(serializers.ModelSerializer):
    # Field specification for "write_only" attribute is a duplicate of "extra_kwargs" option in Meta class.
    # Consider removing the following line:
    # file = serializers.FileField(write_only=True, required=False)

    class Meta:
        model = Multimedia
        fields = ("createdAt",
                  "url",
                  "type",
                  "id",
                  "file",
                  "meta")
        read_only_fields = ("id",
                            "url")
        # "write_only_fields" is a PendingDeprecation and it is replaced with "extra_kwargs" /
        # Source: http://www.django-rest-framework.org/topics/3.0-announcement/#the-extra_kwargs-option
        extra_kwargs = {'file': {'write_only': True}}

    def create(self, validated_data):
        multimedia = Multimedia.objects.create(**validated_data)
        if multimedia.file:
            multimedia.url = "/heritages/{}/{}/{}.png".format(
                multimedia.heritage.id, multimedia.type, multimedia.id)
        multimedia.save()
        heritage_created.send(sender=HeritageSerializer, instance=multimedia.heritage)
        return multimedia


heritage_created = django.dispatch.Signal(providing_args=["instance"])


class HeritageSerializer(serializers.ModelSerializer):
    basicInformation = BasicInformationSerializer(many=True)
    origin = OriginSerializer(many=True)
    tags = TagSerializer(many=True)
    multimedia = MultimediaSerializer(many=True, read_only=True)

    class Meta:
        model = Heritage
        fields = (
            "id",
            "title",
            "description",
            "basicInformation",
            "createdAt",
            "updatedAt",
            "tags",
            "startDate",
            "endDate",
            "exactDate",
            "origin",
            "multimedia")
        read_only_fields = ("id",)

    def create(self, validated_data):
        basic_information = validated_data.pop("basicInformation")
        tags = validated_data.pop("tags")
        origin = validated_data.pop("origin")
        heritage = Heritage.objects.create(**validated_data)

        for entry in basic_information:
            BasicInformation.objects.create(heritage=heritage, **entry)

        for entry in origin:
            Origin.objects.create(heritage=heritage, **entry)

        for entry in tags:
            existing_tags = Tag.objects.filter(name=entry)
            if not existing_tags:
                Tag.objects.create(name=entry)
            heritage_tags = heritage.tags.filter(name=entry)
            if not heritage_tags:
                heritage.tags.add(*Tag.objects.get_or_create(**entry))

        heritage_created.send(sender=self.__class__, instance=heritage)
        return heritage


class SelectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selector
        fields = ("type",
                  "conformsTo",
                  "value")


class AnnotationTargetSerializer(serializers.ModelSerializer):
    selector = SelectorSerializer(many=True)

    class Meta:
        model = AnnotationTarget
        fields = ("target_id",
                  "type",
                  "format",
                  "selector")

    def __init__(self, *args, **kwargs):
        super(AnnotationTargetSerializer, self).__init__(*args, **kwargs)
        self.fields["target_id"].label = "id"

    def create(self, validated_data):
        validated_selector = validated_data.pop("selector")
        target = AnnotationTarget.objects.create(**validated_data)
        for entry in validated_selector:
            Selector.objects.create(target=target, **entry)
        return target


class AnnotationBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnotationBody
        fields = ("type",
                  "value",
                  "format")


class AnnotationSerializer(serializers.ModelSerializer):
    body = AnnotationBodySerializer(many=True)
    target = AnnotationTargetSerializer(many=True)

    class Meta:
        model = Annotation
        fields = ("context",
                  "annotation_id",
                  "type",
                  "motivation",
                  "creator",
                  "created",
                  "body",
                  "target")

    def to_representation(self, instance):
        data = super(AnnotationSerializer, self).to_representation(instance)
        data["@context"] = instance.context
        data["id"] = instance.annotation_id
        del data["context"]
        del data["annotation_id"]
        return data

    def create(self, validated_data):
        validated_body = validated_data.pop("body")
        validated_target = validated_data.pop("target")
        annotation = Annotation.objects.create(heritage=Heritage.objects.get(pk=self.context["heritage_id"]),
                                               **validated_data)

        for entry in validated_body:
            AnnotationBody.objects.create(annotation=annotation, **entry)

        for index, entry in enumerate(validated_target):
            target = AnnotationTarget.objects.create(annotation=annotation,
                                                     target_id=self.context["target_id"][index],
                                                     type=entry["type"],
                                                     format=entry["format"])
            selector_data = entry.pop("selector")
            for data in selector_data:
                Selector.objects.create(target=target,
                                        type=data["type"],
                                        conformsTo=data["conformsTo"],
                                        value=data["value"])

        return annotation


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "username",
                  "email", "password")
        read_only_fields = ["id"]

    def create(self, validated_data):
        password = validated_data["password"]
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data["email"]
        instance.first_name = validated_data["first_name"]
        instance.last_name = validated_data["last_name"]
        instance.set_password(validated_data["password"])
        instance.save()
        return instance
