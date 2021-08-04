# coding:utf-8

from django.conf.urls import url
from .views import views

urlpatterns = [
    url(r'^api/session', views.session),
    url(r'^api/(?P<user_id>\w+)$', views.user)
]
