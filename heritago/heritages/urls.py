from django.conf.urls import url

from heritages import views

urlpatterns = [
    url(r"^$", views.HeritagesListView.as_view()),
    url(r"^(?P<pk>\d+)", views.HeritageView.as_view()),
    url(r"^(?P<heritage_id>\d+)/multimedia$",
        views.MultimediaView.as_view()),

]
