#! /user/bin/env python
# -*- coding:utf-8 -*-

from ..dao import dao2


def service2_get_user(env, user_id):
    """
    :param env:
    :param user_id:
    :return:
    """
    data = {}
    try:
        result = dao2.get_user(env, user_id)
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


def service2_get_user_id(env, user_id):
    """
    :param env:
    :param user_id:
    :return:
    """
    data = None
    try:
        result = dao2.get_user(env, user_id)
        if result:
            data = result.user_id
        else:
            raise ValueError
    except ValueError:
        pass
    finally:
        return data


def service2_delete_user(env, user_id):
    """
    :param env:
    :param user_id:
    :return:
    """
    data = None
    try:
        result = dao2.delete_user(env, user_id)
        if result:
            data = result[0]
        else:
            raise ValueError
    except ValueError:
        pass
    finally:
        return data


def service2_update_user(env, user_id, password, username, email, create_time):
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
        result = dao2.update_user(env, user_id, password, username, email, create_time)
        if result:
            data = result
        else:
            raise ValueError
    except ValueError:
        pass
    finally:
        return data


def service2_create_user(env, user_id, password, username, email, create_time):
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
        result = dao2.create_user(env, user_id, password, username, email, create_time)
        data = {"id": result.id,
                "user_id": result.user_id,
                "password": result.password,
                "username": result.username,
                "email": result.email,
                "create_time": result.create_time}
        if result:
            data = result
        else:
            raise ValueError
    except ValueError:
        pass
    finally:
        return data
