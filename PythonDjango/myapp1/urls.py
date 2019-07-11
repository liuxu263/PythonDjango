#! /usr/bin/python
# -*- coding:utf-8 -*-

''

__author__ = 'lx'

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'homepage/', views.homepage),
    path('login/', views.login),
    path('register/', views.register)
]
