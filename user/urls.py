from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.users, name='users'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^group/$', views.groups, name='groups'),
    url(r'^group/create_group/$', views.create_group, name='create'),
    url(r'^group/(?P<pk>[0-9]+)/edit/$', views.edit_group, name='edit'),
    url(r'^group/delete_group/$', views.delete_group, name='delete'),
    url(r'^group/show_group/(?P<pk>[0-9]+)/$', views.show_group, name='show_group'),
]