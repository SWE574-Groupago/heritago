from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from elasticsearch import Elasticsearch

from heritages.models import Heritage
from heritages.serializers import HeritageSerializer, heritage_created

es = Elasticsearch(settings.ELASTICSEARCH_URL)
index_name = settings.HERITAGE_SEARCH["INDEX"]
type_name = settings.HERITAGE_SEARCH["TYPE"]


@receiver(heritage_created, sender=HeritageSerializer)
def heritage_saved(sender, instance, **kwargs):
    serialized = HeritageSerializer(instance)
    es.index(index_name, type_name, serialized.data, id=instance.id)


@receiver(post_delete, sender=Heritage)
def heritage_deleted(sender, instance, **kwargs):
    es.delete(index_name, type_name, instance.id)


def search_heritages(keyword, size=50, from_record=0):
    query = {
      "from": from_record,
      "size": size,
      "query": {
        "match": {
          "_all": keyword
        }
      }
    }
    return es.search(index_name, type_name, query)


def search_annotations(keyword, size=50, from_record=0):
    query = {
      "from": from_record,
      "size": size,
      "query": {
        "match": {
          "_all": keyword
        }
      }
    }
    return es.search(index_name, type_name, query)
