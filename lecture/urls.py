from django.conf.urls import url
from lecture import views

urlpatterns = [
    url(r'^$', views.lectures, name='groups'),
    #url(r'^create/$', views.create, name='create'),
    #url(r'^(?P<pk>[0-9]+)/edit/$', views.edit, name='edit'),
    #url(r'^delete/$', views.delete, name='delete'),
    #url(r'^show_lecture/(?P<pk>[0-9]+)/$', views.show, name='show_group'),
    #url(r'^(?P<pk>[0-9]+)/add_member/$', views.add_member, name='add_member')
]