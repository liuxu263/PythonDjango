#! /usr/bin/python
# -*- coding:utf-8 -*-

''

__author__ = 'lx'

from django.contrib import admin
from .models import Post, Category, Tag

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
