# ! /usr/bin/python
# -*- coding:utf-8 -*-

''

__author__ = 'lx'

from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'templates/blog/index.html', context={
        'post_list': post_list
    })
