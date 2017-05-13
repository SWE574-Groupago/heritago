from rest_framework import serializers

from heritages.models import Heritage, BasicInformation, Origin, Tag, Multimedia, UserProfile

from django.contrib.auth.models import User


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
    file = serializers.FileField(write_only=True)

    class Meta:
        model = Multimedia
        fields = ("createdAt", "url", "type", "id", "file", "meta")
        write_only_fields = ("file",)
        read_only_fields = ("id", "url",)

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

        for entry in basic_information:
            BasicInformation.objects.create(heritage=heritage, **entry)

        for entry in origin:
            Origin.objects.create(heritage=heritage, **entry)

        for entry in tags:
            # TODO: test to ensure tags are not duplicated
            heritage.tags.add(*Tag.objects.get_or_create(**entry))

        return heritage




