#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

''

__author__ = 'lx'


def check_password_diff(password, password1):
    if password != password1:
        return False


def check_password_length(password):
    if len(password) <= 8:
        return False
