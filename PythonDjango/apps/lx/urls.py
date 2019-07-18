#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

''

__author__ = 'lx'

from django.urls import path
from django.conf.urls import url, include
from .lxuser import registerviews

urlpatterns = [
    url(r'register/', registerviews.register)
]
