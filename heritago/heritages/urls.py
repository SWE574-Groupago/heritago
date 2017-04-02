from django.conf.urls import url

from heritages import views

urlpatterns = [
    url(r"^$", views.HeritagesList.as_view()),
    url(r"^(?P<recipe_id>\d+)/multimedia$",
        views.MultimediaView.as_view()),

]
