#! /user/bin/env python
# -*- coding:utf-8 -*-

import logging
from ..dao import dao3

info_logger = logging.getLogger('django')
error_logger = logging.getLogger('error')


def service3_get_user(env, user_id):
    """
    :param env:
    :param user_id:
    :return:
    """
    data = {}
    try:
        result = dao3.get_user(env, user_id)
        data = {"id": result.id,
                "user_id": result.user_id,
                "password": result.password,
                "username": result.username,
                "email": result.email,
                "create_time": result.create_time}
        info_logger.info("info1")
        info_logger.error("error1")
        error_logger.error("error2")
        if result:
            return data
        else:
            raise ValueError
    except ValueError:
        pass
    finally:
        return data


def service3_get_user_id(env, user_id):
    """
    :param env:
    :param user_id:
    :return:
    """
    data = None
    try:
        result = dao3.get_user(env, user_id)
        if result:
            data = result.user_id
        else:
            raise ValueError
    except ValueError:
        pass
    finally:
        return data


def service3_delete_user(env, user_id):
    """
    :param env:
    :param user_id:
    :return:
    """
    data = False
    try:
        result = dao3.delete_user(env, user_id)
        if result:
            data = True
        else:
            raise ValueError
    except ValueError:
        pass
    finally:
        return data


def service3_update_user(env, user_id, password, username, email, create_time):
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
        result = dao3.update_user(env, user_id, password, username, email, create_time)
        if result:
            data = True
        else:
            raise ValueError
    except ValueError:
        pass
    finally:
        return data


def service3_create_user(env, user_id, password, username, email, create_time):
    """
    :param env:
    :param user_id:
    :param password:
    :param username:
    :param email:
    :param create_time:
    :return:
    """
    data = {}
    try:
        result = dao3.create_user(env, user_id, password, username, email, create_time)
        data = {"id": result.id,
                "user_id": result.user_id,
                "password": result.password,
                "username": result.username,
                "email": result.email,
                "create_time": result.create_time}
        if result:
            return data
        else:
            raise ValueError
    except ValueError:
        pass
    finally:
        return data
