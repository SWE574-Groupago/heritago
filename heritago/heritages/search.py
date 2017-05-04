from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from elasticsearch import Elasticsearch

from heritages.models import Heritage
from heritages.serializers import HeritageSerializer

es = Elasticsearch(settings.ELASTICSEARCH_URL)
index_name = settings.HERITAGE_SEARCH["INDEX"]
type_name = settings.HERITAGE_SEARCH["TYPE"]


@receiver(post_save, sender=Heritage)
def heritage_saved(sender, instance, **kwargs):
    serialized = HeritageSerializer(instance)
    es.index(index_name, type_name, serialized.data, id=instance.id)
    print("sending to elastic...")
    print(sender)


@receiver(post_delete, sender=Heritage)
def heritage_deleted(sender, instance, **kwargs):
    es.delete(index_name, type_name, instance.id)
