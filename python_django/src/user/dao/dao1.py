#! /user/bin/env python
# -*- coding:utf-8 -*-

import logging
from python_django.common.database_manager1 import MysqlManager

logger = logging.getLogger('django')


def get_user(env, user_id):
    """
    :param env:
    :param user_id:
    :return:
    """
    try:
        mysql_manager = MysqlManager(env)
        sql = "select * from user where user_id = %s"
        param = (str(user_id),)
        result = mysql_manager.select(sql, param)
        logger.info("dao get user")
        if type(result) is tuple and len(result) > 0:
            data = result
            return data
        else:
            raise KeyError
    except KeyError:
        raise KeyError
    finally:
        pass


def delete_user(env, user_id):
    """
    :param env:
    :param user_id:
    :return:
    """
    data = False
    try:
        mysql_manager = MysqlManager(env)
        sql = "delete from user where user_id = %s"
        param = (str(user_id),)
        result = mysql_manager.cud(sql, param)
        if result and result == 1:
            data = True
        else:
            raise ValueError
    except ValueError:
        pass
    finally:
        return data


def update_user(env, user_id, password, username, email, create_time):
    """
    :param env:
    :param user_id:
    :param password:
    :param username:
    :param email:
    :param create_time:
    :return:
    """
    data = False
    try:
        mysql_manager = MysqlManager(env)
        sql = "update user " \
              "set user_id = %s ,password = %s ,username = %s ,email = %s ,create_time = %s where user_id = %s"
        param = (str(user_id), str(password), str(username), str(email), str(create_time), str(user_id))
        result = mysql_manager.cud(sql, param)
        if result and result == 1:
            data = True
        else:
            raise ValueError
    except ValueError:
        pass
    finally:
        return data


def create_user(env, user_id, password, username, email, create_time):
    """
    :param env:
    :param user_id:
    :param password:
    :param username:
    :param email:
    :param create_time:
    :return:
    """
    data = False
    try:
        mysql_manager = MysqlManager(env)
        sql = "insert into user (`user_id`,`password`,`username`,`email`,`create_time`) values (%s,%s,%s,%s,%s)"
        param = (str(user_id), str(password), str(username), str(email), str(create_time))
        result = mysql_manager.cud(sql, param)
        if result and result == 1:
            data = True
        else:
            raise ValueError
    except ValueError:
        pass
    finally:
        return data
