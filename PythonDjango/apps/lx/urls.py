#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

''

__author__ = 'lx'

from django.urls import path
from django.conf.urls import url, include
from .lx_user import register_views

urlpatterns = [
    url(r'register/', register_views.register)
]
