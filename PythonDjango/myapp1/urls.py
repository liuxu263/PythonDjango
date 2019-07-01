#! /usr/bin/python
# -*- coding:utf-8 -*-

''

__author__ = 'lx'

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.hoempage),
    path('login/', views.login),
    path('register/', views.register)
]
