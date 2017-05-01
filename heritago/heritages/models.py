import os

from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.TextField(max_length=100)


class Heritage(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    title = models.TextField(max_length=255, null=False)
    description = models.TextField(null=False)
    annotationCount = models.IntegerField(default=0)
    tags = models.ManyToManyField(to=Tag, related_name="tags")

    def delete(self, using=None, keep_parents=False):
        for m in self.multimedia.all():
            m.delete()
        return super().delete(using, keep_parents)


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
    createdAt = models.DateTimeField(auto_now_add=True)
    type = models.CharField(choices=CATEGORIES.to_set(), max_length=10)
    url = models.URLField()
    file = models.FileField(upload_to="uploads/")

    def delete(self, using=None, keep_parents=False):
        os.remove(os.path.join(self.file.name))
        return super().delete(using, keep_parents)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    email = models.EmailField('email', null=True)
    note = models.TextField('Notes', blank=True, null=True)

    def __unicode__(self):
        return self.user.username


