from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^user/$', views.user, name='user'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<room_id>[0-9]+)/$', views.show_user, name='user'),
    url(r'^create/$', views.create, name='create'),
    url(r'^delete/$', views.delete, name='delete'),
]