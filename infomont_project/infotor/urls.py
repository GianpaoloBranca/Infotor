from django.conf.urls import url
from infotor import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<torrent_id>[0-9]+)/$', views.show_torrent, name='show_torrent')
]
