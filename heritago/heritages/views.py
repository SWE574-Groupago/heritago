# from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.uploadedfile import UploadedFile
from django.conf import settings
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from django.shortcuts import (render, render_to_response, redirect)
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from heritages.models import Heritage, Multimedia, Annotation
from heritages.search import search_heritages, search_annotations
from heritages.serializers import HeritageSerializer, MultimediaSerializer, AnnotationSerializer
from .forms import MyRegistrationForm
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserProfileForm
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

json_ld_content_type = "application/ld+json; profile=\"http://www.w3.org/ns/anno.jsonld\""


class HeritagesListView(generics.ListCreateAPIView):
    queryset = Heritage.objects.all()
    serializer_class = HeritageSerializer

    def list(self, request, *args, **kwargs):
        keyword = self.request.query_params.get("keyword", None)
        if not keyword:
            return super().list(request, *args, **kwargs)

        result = Response(search_heritages(keyword)).data
        return Response(i["_source"] for i in result["hits"]["hits"])


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

    @staticmethod
    def get_file(request, multimedia_id):
        try:
            m = Multimedia.objects.get(pk=multimedia_id)
        except ObjectDoesNotExist:
            raise NotFound(multimedia_id)
        file = UploadedFile(m.file)
        return HttpResponse(file, content_type="image/png")


class AnnotationListView(generics.ListCreateAPIView):
    serializer_class = AnnotationSerializer

    def get_queryset(self):
        queryset = Annotation.objects.all()
        heritage_id = self.kwargs["heritage_id"]
        if heritage_id is not None:
            queryset = queryset.filter(target__target_id__contains=heritage_id)
            return queryset
        else:
            return NotFound()

    def get_serializer_context(self):
        return {"target_id": self.request.build_absolute_uri(),
                "heritage_id": self.kwargs["heritage_id"]}

    def list(self, request, *args, **kwargs):
        keyword = self.request.query_params.get("keyword", None)
        if not keyword:
            return super().list(request, *args, **kwargs)

        result = Response(search_annotations(keyword)).data
        return Response(i["_source"] for i in result["hits"]["hits"])


class AnnotationView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response(settings.STATIC_URL + 'login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/profile')
    else:
        return HttpResponseRedirect('/invalid')


def invalid_login(request):
    return render_to_response(settings.STATIC_URL + 'invalid_loggedin.html')


def logout(request):
    auth.logout(request)
    return render_to_response(settings.STATIC_URL + 'logout.html')


def register_user(request):
    if request.method == 'POST':
        user_form = MyRegistrationForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST, files=request.FILES)
        # Check if forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile_form.instance.user = user
            profile_form.save()

            return HttpResponseRedirect('/register_success')

    else:
        user_form = MyRegistrationForm()
        profile_form = UserProfileForm()
    args = {}
    args.update(csrf(request))

    args['user_form'] = user_form
    args['profile_form'] = profile_form

    return render_to_response(settings.STATIC_URL + 'register.html', args)


@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile')

    else:
        user = request.user
        profile = user.profile

        form = UserProfileForm(instance=profile)

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render(request, settings.STATIC_URL + 'profile.html', args)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password-change')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, settings.STATIC_URL + 'change_password.html', {
        'form': form
    })
