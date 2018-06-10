from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(regex=r'^details/(?P<id>\d+)/$', view=views.details, name='details'),


]
