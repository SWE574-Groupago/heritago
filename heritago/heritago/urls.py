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
from django.contrib.auth.views import password_reset



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"api/v1/heritages/", include("heritages.urls")),

# user auth urls

   # url(r'^$', views.diary, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^auth/$', views.auth_view, name='auth_view'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^loggedin/$', views.loggedin, name='loggedin'),
    url(r'^invalid/$', views.invalid_login, name='invalid_login'),
    url(r'^register/$', views.register_user, name='register_user'),
    url(r'^profile/$', views.user_profile, name='user_profile'),
    url(r'^change_password/$', views.change_password , name='password-change'),



]
