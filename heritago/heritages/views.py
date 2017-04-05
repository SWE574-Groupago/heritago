from rest_framework import generics

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

    def perform_create(self, serializer):
        heritage_id = self.kwargs["heritage_id"]
        heritage = Heritage.objects.get(pk=heritage_id)
        return serializer.save(heritage=heritage)

