from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.schedule, name='schedule'),
    url(r'^group_schedule/$', views.group_schedule, name='delete'),

]