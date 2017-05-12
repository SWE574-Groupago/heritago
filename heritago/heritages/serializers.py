from rest_framework import serializers

from heritages.models import Heritage, BasicInformation, Origin, Tag, Multimedia, Selector, AnnotationTarget, \
    AnnotationBody, Annotation


class BasicInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicInformation
        fields = ("name", "value", )


class OriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origin
        fields = ("name", )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name", )


class MultimediaSerializer(serializers.ModelSerializer):
    # Field specification for "write_only" attribute is a duplicate of "extra_kwargs" option in Meta class.
    class Meta:
        model = Multimedia
        fields = ("createdAt", "url", "type", "id", "file", "meta")
        read_only_fields = ("id", "url",)
        # "write_only_fields" is a PendingDeprecation and it is replaced with "extra_kwargs" /
        # Source: http://www.django-rest-framework.org/topics/3.0-announcement/#the-extra_kwargs-option
        extra_kwargs = {'file': {'write_only': True}}

    def create(self, validated_data):
        multimedia = Multimedia.objects.create(**validated_data)
        multimedia.url = "/heritages/{}/{}/{}.png".format(
            multimedia.heritage.id, multimedia.type, multimedia.id)
        multimedia.save()
        return multimedia


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
        read_only_fields = ("id", )

    def create(self, validated_data):
        basic_information = validated_data.pop("basicInformation")
        tags = validated_data.pop("tags")
        origin = validated_data.pop("origin")
        heritage = Heritage.objects.create(**validated_data)
        tag_set = set()

        for entry in basic_information:
            BasicInformation.objects.create(heritage=heritage, **entry)

        for entry in origin:
            Origin.objects.create(heritage=heritage, **entry)

        for entry in tags:
            tag_set.add(entry)

        for entry in tag_set:
            heritage.tags.add(*Tag.objects.get_or_create(**entry))

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
        fields = ("id",
                  "type",
                  "format",
                  "selector")

    def create(self, validated_data):
        validated_selector = validated_data.pop("selector")
        target = AnnotationTarget.objects.create(**validated_data)

        for entry in validated_selector:
            Selector.objects.create(target=target, **entry)


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
                  "id",
                  "type",
                  "creator",
                  "created",
                  "body",
                  "target")

    def __init__(self, *args, **kwargs):
        super(AnnotationSerializer, self).__init__(*args, **kwargs)
        self.fields["context"].label = "@context"

    def create(self, validated_data):
        validated_body = validated_data.pop("body")
        validated_target = validated_data.pop("target")
        annotation = Annotation.objects.create(**validated_data)

        for entry in validated_body:
            AnnotationBody.objects.create(annotation=annotation, **entry)

        for entry in validated_target:
            AnnotationSerializer.objects.create(annotation=annotation, **entry)

        return annotation
