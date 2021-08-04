# coding:utf-8
from ..dao import dao3


def service1_select():
    """
    :return:
    """
    data = dao3.select()
    return data


def service1_delete():
    """
    :return:
    """
    data = dao3.delete()
    return data


def service1_update():
    """
    :return:
    """
    data = dao3.update()
    return data


def service1_insert():
    """
    :return:
    """
    # data = dao1.insert()
    return "hello world"
