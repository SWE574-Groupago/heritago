import os

from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
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

    startDate = models.TextField(null=True, default="", blank=True)
    endDate = models.TextField(null=True, default="", blank=True)
    exactDate = models.TextField(null=True, default="", blank=True)

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

    heritage = models.ForeignKey(to=Heritage, related_name="multimedia", on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    type = models.CharField(choices=CATEGORIES.to_set(), max_length=10)
    url = models.URLField(blank=True)
    file = models.FileField(upload_to="uploads/", blank=True, null=True)
    meta = models.TextField(blank=True)

    def delete(self, using=None, keep_parents=False):
        os.remove(os.path.join(self.file.name))
        return super().delete(using, keep_parents)


class Annotation(models.Model):
    heritage = models.ForeignKey(to=Heritage, related_name="annotation", on_delete=models.CASCADE)
    context = models.URLField(null=False, default="http://www.w3.org/ns/anno.jsonld")
    annotation_id = models.URLField(max_length=255, default="http://574heritago.com/annotations/null/")
    type = models.CharField(max_length=255, null=False, default="Annotation")
    creator = models.CharField(max_length=255, null=False)
    created = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(null=False, default=0)


class AnnotationBody(models.Model):
    class TYPES(object):
        VIDEO = "video"
        AUDIO = "audio"
        IMAGE = "image"
        LOCATION = "location"
        TEXT = "text"

        @classmethod
        def to_set(cls):
            return (
                ("video", cls.VIDEO),
                ("audio", cls.AUDIO),
                ("image", cls.IMAGE),
                ("location", cls.LOCATION),
                ("text", cls.TEXT))

    class MIMES(object):
        PLAINTEXT = "text/plain"
        MPEGVIDEO = "video/mpeg"
        AVIVIDEO = "video/avi"
        PNGIMAGE = "image/png"
        BMPIMAGE = "image/bmp"
        GIFIMAGE = "image/gif"
        JPEGIMAGE = "image/jpeg"
        MIDIAUDIO = "audio/midi"
        MPEGAUDIO = "audio/mpeg"

        @classmethod
        def to_set(cls):
            return (
                ("text/plain", cls.PLAINTEXT),
                ("video/mpeg", cls.MPEGVIDEO),
                ("video/avi", cls.AVIVIDEO),
                ("image/png", cls.PNGIMAGE),
                ("image/bmp", cls.BMPIMAGE),
                ("image/gif", cls.GIFIMAGE),
                ("image/jpeg", cls.JPEGIMAGE),
                ("audio/midi", cls.MIDIAUDIO),
                ("audio/mpeg", cls.MPEGAUDIO))

    annotation = models.ForeignKey(to=Annotation, related_name="body", on_delete=models.CASCADE)
    type = models.CharField(choices=TYPES.to_set(), max_length=10)
    format = models.CharField(choices=MIMES.to_set(), max_length=15)
    value = models.CharField(max_length=255, null=False)


class AnnotationTarget(models.Model):
    class TYPES(object):
        VIDEO = "video"
        AUDIO = "audio"
        IMAGE = "image"
        LOCATION = "location"
        TEXT = "text"

        @classmethod
        def to_set(cls):
            return (
                ("video", cls.VIDEO),
                ("audio", cls.AUDIO),
                ("image", cls.IMAGE),
                ("location", cls.LOCATION),
                ("text", cls.TEXT))

    class MIMES(object):
        PLAINTEXT = "text/plain"
        MPEGVIDEO = "video/mpeg"
        AVIVIDEO = "video/avi"
        PNGIMAGE = "image/png"
        BMPIMAGE = "image/bmp"
        GIFIMAGE = "image/gif"
        JPEGIMAGE = "image/jpeg"
        MIDIAUDIO = "audio/midi"
        MPEGAUDIO = "audio/mpeg"

        @classmethod
        def to_set(cls):
            return (
                ("text/plain", cls.PLAINTEXT),
                ("video/mpeg", cls.MPEGVIDEO),
                ("video/avi", cls.AVIVIDEO),
                ("image/png", cls.PNGIMAGE),
                ("image/bmp", cls.BMPIMAGE),
                ("image/gif", cls.GIFIMAGE),
                ("image/jpeg", cls.JPEGIMAGE),
                ("audio/midi", cls.MIDIAUDIO),
                ("audio/mpeg", cls.MPEGAUDIO))

    annotation = models.ForeignKey(to=Annotation, related_name="target", on_delete=models.CASCADE)
    target_id = models.CharField(max_length=255, null=False, default="http://574heritago.com/heritages/null/")
    type = models.CharField(choices=TYPES.to_set(), max_length=10)
    format = models.CharField(choices=MIMES.to_set(), max_length=15)


# W3C Specification for selectors at https://www.w3.org/TR/annotation-model/#selectors
class Selector(models.Model):
    class SPECIFICATIONS(object):
        TEXT = "http://tools.ietf.org/rfc/rfc5147"
        MEDIA = "http://www.w3.org/TR/media-frags/"
        IMAGE = "http://www.w3.org/TR/SVG/"

        @classmethod
        def to_set(cls):
            return (
                ("http://tools.ietf.org/rfc/rfc5147", cls.TEXT),
                ("http://www.w3.org/TR/media-frags/", cls.MEDIA),
                ("http://www.w3.org/TR/SVG/", cls.IMAGE))

    target = models.ForeignKey(to=AnnotationTarget, related_name="selector", on_delete=models.CASCADE)
    type = models.CharField(default="FragmentSelector", max_length=25, null=False)
    conformsTo = models.CharField(choices=SPECIFICATIONS.to_set(), max_length=50)
    value = models.CharField(max_length=255, null=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    email = models.EmailField('email', null=True)
    note = models.TextField('Notes', blank=True, null=True)

    def __unicode__(self):
        return self.user.username


@receiver(post_save, sender=Annotation, dispatch_uid="annotation_id_setter")
def annotation_id_setter(sender, instance, **kwargs):
    annotation_id = "http://574heritago.com/annotations/{}/".format(instance.id)
    instance.annotation_id = annotation_id
