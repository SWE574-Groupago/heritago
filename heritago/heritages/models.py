from django.db import models


class Tag(models.Model):
    # heritage = models.ForeignKey(to=Heritage, related_name="tags", on_delete=models.CASCADE)
    name = models.TextField(max_length=100)


class Heritage(models.Model):
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)
    title = models.TextField(max_length=255, null=False)
    description = models.TextField(null=False)
    annotationCount = models.IntegerField(default=0)
    tags = models.ManyToManyField(to=Tag,related_name="tags")


class Origin(models.Model):
    heritage = models.ForeignKey(to=Heritage, related_name="origin", on_delete=models.CASCADE)
    name = models.TextField(max_length=100)


class BasicInformation(models.Model):
    heritage = models.ForeignKey(to=Heritage, related_name="basicInformation", on_delete=models.CASCADE)
    name = models.TextField(max_length=255, null=False)
    value = models.TextField(null=False)


class Multimedia(models.Model):

    class CATEGORIES(object):
        VIDEO = "video"
        AUDIO = "audio"
        IMAGE = "image"
        LOCATION = "location"

        @classmethod
        def to_set(cls):
            return (
                ("video", cls.VIDEO),
                ("audio", cls.AUDIO),
                ("image", cls.IMAGE),
                ("location", cls.LOCATION))
    heritage = models.ForeignKey(
        to=Heritage, related_name="multimedia", on_delete=models.CASCADE)
    createdAt = models.DateField(auto_now_add=True)
    type = models.CharField(choices=CATEGORIES.to_set(), max_length=10)
    url = models.URLField()

    #             "type": "video",
    #             "id": 51,
    #             "url": "http://www.heritago.com/heritages/1/videos/51.mp4",
    #             "createdAt": "2017-01-19 11:11:12+3"
    #
    #
    # desc
    # {
    #     "id": 1,
    #     "description": "",
    #     "title": "",
    #     "createdAt": "2017-01-19 11:11:11+3",
    #     "basicInformation": [
    #         {
    #             "key": "completed",
    #             "value": "1991"
    #         },
    #         {
    #             "key": "author",
    #             "value": "Namik Kemal"
    #         }
    #     ],
    #     "origins": [
    #         "Turkish",
    #         "Hittit"
    #     ],
    #     "tags": [
    #         "building",
    #         "history",
    #         "food"
    #     ],
    #     "annotationCount": 32,
    #     "owner": {
    #         "id": 1,
    #         "name": "Suzan U."
    #     },
    #     "multimedia": [
    #         {
    #             "type": "image",
    #             "id": 132,
    #             "url": "http://www.heritago.com/heritages/1/images/132.png",
    #             "createdAt": "2017-01-19 11:11:12+3"
    #         },
    #         {
    #             "type": "video",
    #             "id": 51,
    #             "url": "http://www.heritago.com/heritages/1/videos/51.mp4",
    #             "createdAt": "2017-01-19 11:11:12+3"
    #         },
    #         {
    #             "type": "audio",
    #             "id": 22,
    #             "url": "http://www.heritago.com/heritages/1/audio/22.mp3",
    #             "createdAt": "2017-01-19 11:11:12+3"
    #         },
    #         {
    #             "type": "location",
    #             "id": 61,
    #             "url": "http://www.heritago.com/heritages/1/videos/51.png",
    #             "createdAt": "2017-01-19 11:11:12+3",
    #             "selector": {
    #                 "type": "polygon",
    #                 "value": {
    #                     "latlongs": [
    #                         [
    #                             12.2,
    #                             58.7
    #                         ],
    #                         [
    #                             71.5,
    #                             95.4
    #                         ]
    #                     ]
    #                 }
    #             }
    #         }
    #     ]
    # }