#! /user1/bin/env python
# -*- coding:utf-8 -*-


from python_django.src.user1.models.user import User


class UserDao(object):
    def __init__(self):
        self._user = User()

    def _select(self):
        self._user.objects.all()

    def select(self):
        return self._select()
