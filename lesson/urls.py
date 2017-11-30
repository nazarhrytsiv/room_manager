from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lessons, name='lessons'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^delete/$', views.delete, name='delete')
]