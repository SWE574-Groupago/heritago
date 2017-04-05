from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.exceptions import NotFound

from heritages.models import Heritage, Multimedia
from heritages.serializers import HeritageSerializer, MultimediaSerializer


class HeritagesListView(generics.ListCreateAPIView):
    queryset = Heritage.objects.all()
    serializer_class = HeritageSerializer


class HeritageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Heritage.objects.all()
    serializer_class = HeritageSerializer


class MultimediaView(generics.ListCreateAPIView):
    queryset = Multimedia.objects.all()
    serializer_class = MultimediaSerializer

    def get_queryset(self):
        try:
            heritage = Heritage.objects.get(pk=self.kwargs["heritage_id"])
        except ObjectDoesNotExist:
            raise NotFound()
        return heritage.multimedia

    def perform_create(self, serializer):
        heritage_id = self.kwargs["heritage_id"]
        try:
            heritage = Heritage.objects.get(pk=heritage_id)
        except ObjectDoesNotExist:
            raise NotFound()
        return serializer.save(heritage=heritage)

