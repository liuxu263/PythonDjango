#! /user/bin/env python
# -*- coding:utf-8 -*-

# coding:utf-8
from ..dao import dao1


def service1_select(env, *args, **kwargs):
    """
    :param env:
    :param args:
    :param kwargs:
    :return:
    """
    data = dao1.select(env)
    return data


def service1_delete(env, *args, **kwargs):
    """
    :param env:
    :param args:
    :param kwargs:
    :return:
    """
    data = dao1.delete(env)
    return data


def service1_update(env, *args, **kwargs):
    """
    :param env:
    :param args:
    :param kwargs:
    :return:
    """
    data = dao1.update(env)
    return data


def service1_insert(env, *args, **kwargs):
    """
    :param env:
    :param args:
    :param kwargs:
    :return:
    """
    data = dao1.insert(env)
    return data
