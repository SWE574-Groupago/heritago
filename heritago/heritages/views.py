from django.core.exceptions import ObjectDoesNotExist
from django.core.files.uploadedfile import UploadedFile
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.viewsets import ViewSet
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.shortcuts import (render_to_response, render)

from heritages.models import Heritage, Multimedia
from heritages.serializers import HeritageSerializer, MultimediaSerializer


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

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)