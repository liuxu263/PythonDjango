#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

''

__author__ = 'lx'

from ..models import User


def check_email_diff(email):
    if User.objects.filter(email=email):
        return False
