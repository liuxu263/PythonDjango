#! /user/bin/env python
# -*- coding:utf-8 -*-

from rest_framework import serializers
from ..models.user1 import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'username', 'password', 'email', 'create_time')

