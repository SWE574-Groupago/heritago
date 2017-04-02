from rest_framework import generics

from heritages.models import Heritage, Multimedia
from heritages.serializers import HeritageSerializer, MultimediaSerializer


class HeritagesList(generics.ListCreateAPIView):
    queryset = Heritage.objects.all()
    serializer_class = HeritageSerializer


class MultimediaView(generics.ListCreateAPIView):
    queryset = Multimedia.objects.all()
    serializer_class = MultimediaSerializer

    def perform_create(self, serializer):
        heritage_id = self.kwargs["heritage_id"]
        heritage = Heritage.objects.get(pk=heritage_id)
        serializer.save(heritage=heritage)

