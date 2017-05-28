from django.conf.urls import url
from heritages import views

urlpatterns = [
    url(r"^$", views.HeritagesListView.as_view()),
    url(r"^(?P<pk>\d+)$", views.HeritageView.as_view()),
    url(r"^(?P<heritage_id>\d+)/multimedia$",
        views.MultimediaListView.as_view()),
    url(r"^(?P<heritage_id>\d+)/multimedia/(?P<pk>\d+)$",
        views.MultimediaView.as_view()),
    url(r"^.*/(image|video|audio|location)/(?P<multimedia_id>\d+)",
        views.MultimediaFileView.as_view({"get": "get_file"})),
    url(r"^(?P<heritage_id>\d+)/annotations$", views.AnnotationListView.as_view()),
    url(r"^(?P<heritage_id>\d+)/annotations/(?P<pk>\d+)$", views.AnnotationView.as_view()),
]
