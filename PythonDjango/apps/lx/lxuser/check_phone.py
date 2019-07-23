#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

''

__author__ = 'lx'

from ..models import User


def check_phone_diff(phone):
    if User.objects.filter(phone=phone):
        return False
