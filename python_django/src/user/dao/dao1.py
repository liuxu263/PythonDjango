#! /user/bin/env python
# -*- coding:utf-8 -*-


from python_django.common.database_manager1 import MysqlManager


def select(env, *args, **kwargs):
    mysql_manager = MysqlManager(env)
    sql = ""
    param = None
    return mysql_manager.select(sql, param)


def delete(env, *args, **kwargs):
    mysql_manager = MysqlManager(env)
    sql = ""
    param = None
    return mysql_manager.cud(sql, param)


def update(env, *args, **kwargs):
    mysql_manager = MysqlManager(env)
    sql = ""
    param = None
    return mysql_manager.cud(sql, param)


def insert(env, *args, **kwargs):
    mysql_manager = MysqlManager(env)
    sql = ""
    param = None
    return mysql_manager.cud(sql, param)
