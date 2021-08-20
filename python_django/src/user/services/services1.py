#! /user/bin/env python
# -*- coding:utf-8 -*-

import logging
from ..dao import dao1

logger = logging.getLogger('django')


def service1_get_user(env, user_id):
    """
    :param env:
    :param user_id:
    :return:
    """
    try:
        result = dao1.get_user(env, user_id)
        logger.info("get user" + result)
        if type(result) is tuple and len(result) > 0:
            data = result[0]
            return data
        else:
            raise KeyError
    except KeyError:
        raise KeyError
    finally:
        pass


def services_is_user(env, user_id):
    """
    :param env:
    :param user_id:
    :return:
    """
    try:
        result = dao1.get_user(env, user_id)
        if result[0].get("user_id") == user_id:
            pass
        else:
            raise KeyError
    except KeyError:
        raise KeyError
    finally:
        pass


def service1_delete_user(env, user_id):
    """
    :param env:
    :param user_id:
    :return:
    """
    data = None
    try:
        result = dao1.delete_user(env, user_id)
        if result:
            data = result
        else:
            raise ValueError
    except ValueError:
        pass
    finally:
        return data


def service1_update_user(env, user_id, password, username, email, create_time):
    """
    :param env:
    :param user_id:
    :param password:
    :param username:
    :param email:
    :param create_time:
    :return:
    """
    data = None
    try:
        result = dao1.update_user(env, user_id, password, username, email, create_time)
        if result:
            data = result
        else:
            raise ValueError
    except ValueError:
        pass
    finally:
        return data


def service1_create_user(env, user_id, password, username, email, create_time):
    """
    :param env:
    :param user_id:
    :param password:
    :param username:
    :param email:
    :param create_time:
    :return:
    """
    data = None
    try:
        result = dao1.create_user(env, user_id, password, username, email, create_time)
        if result:
            data = result
        else:
            raise ValueError
    except ValueError:
        pass
    finally:
        return data
