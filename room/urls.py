from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^room/$', views.room, name='room'),
    url(r'^room/(?P<pk>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^room/(?P<room_id>[0-9]+)/$', views.show_room, name='room'),
    url(r'^room/create/$', views.create, name='create'),
    url(r'^room/delete/$', views.delete, name='delete'),
]
