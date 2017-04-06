import os

from django.core.exceptions import ObjectDoesNotExist
from django.core.files.uploadedfile import UploadedFile
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import mixins
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from heritages.models import Heritage, Multimedia
from heritages.serializers import HeritageSerializer, MultimediaSerializer
from heritago import settings


class HeritagesListView(generics.ListCreateAPIView):
    queryset = Heritage.objects.all()
    serializer_class = HeritageSerializer


class HeritageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Heritage.objects.all()
    serializer_class = HeritageSerializer


class MultimediaListView(generics.ListCreateAPIView):
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


class MultimediaView(generics.RetrieveDestroyAPIView):
    queryset = Multimedia.objects.all()
    serializer_class = MultimediaSerializer


class MultimediaFileView(ViewSet):

    def get_file(self, request, heritage_id, multimedia_id):
        try:
            m = Multimedia.objects.get(pk=multimedia_id)
        except ObjectDoesNotExist:
            raise NotFound(multimedia_id)
        file = UploadedFile(m.file)
        return HttpResponse(file, content_type="image/png")

