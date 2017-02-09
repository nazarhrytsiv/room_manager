from django.conf.urls import url
from group import views

urlpatterns = [
    url(r'^$', views.groups, name='groups'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^show_group/(?P<pk>[0-9]+)/$', views.show, name='show_group'),
]