#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

''

__author__ = 'lx'

from ..models import User


def check_nickname_diff(nickname):
    if User.objects.filter(nickname=nickname):
        print(User.objeckts.filter(nickname=nickname))
        return True
