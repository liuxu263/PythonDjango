# ! /usr/bin/python
# -*- coding:utf-8 -*-

''

__author__ = 'lx'

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'templates/blog/index.html', context={
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客首页'
    })
