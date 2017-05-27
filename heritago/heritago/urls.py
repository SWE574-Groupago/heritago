"""heritago URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from heritages import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"api/users", views.UserDetail)
router.register(r"api/users", views.Users)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"api/v1/heritages/", include("heritages.urls")),
    url(r"^api/users/me$", views.UserDetail.as_view({"get": "get_me"})),
    # url(r"api/v1/annotations/", views.AnnotationListView.as_view()),
    # url(r"api/v1/annotations/(?P<pk>\d+)$", views.AnnotationView.as_view()),

    # user auth urls
    # url(r'^$', views.diary, name='home'),
    # url(r'^login/$', views.login, name='login'),
    # url(r'^auth/$', views.auth_view, name='auth_view'),
    # url(r'^logout/$', views.logout, name='logout'),
    # url(r'^invalid/$', views.invalid_login, name='invalid_login'),
    # url(r'^register/$', views.register_user, name='register_user'),
    # url(r'^profile/$', views.user_profile, name='user_profile'),
    # url(r'^change_password/$', views.change_password , name='password-change'),
]

urlpatterns += router.urls
