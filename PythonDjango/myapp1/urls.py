#! /usr/bin/python
# -*- coding:utf-8 -*-

''

__author__ = 'lx'

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
]
