# coding:utf-8

from django.conf.urls import url
from .views import views1
from .views import views2
from .views import views3

urlpatterns = [
    # url(r'^api/session', views.session),
    url(r'^api/(?P<user_id>\w+)/$', views1.user)
]
