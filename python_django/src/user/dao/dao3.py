# coding:utf-8

from ..models.user3 import User
from python_django.common.database_manager3 import MysqlManager


def get_user(env, user_id):
    """
    :param env:
    :param user_id:
    :return:
    """
    data = None
    try:
        mysql_manager = MysqlManager(env)
        session = mysql_manager.connect_db()
        db_session = session()
        result = db_session.query(User).filter(User.user_id == user_id).first()
        if result:
            data = result
        else:
            raise ValueError
        mysql_manager.connect_db()
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
        session = mysql_manager.connect_db()
        db_session = session()
        result = db_session.query(User).filter(User.user_id == user_id).update(
            {'password': password,
             'username': username,
             'email': email,
             'create_time': create_time})
        db_session.commit()
        if result and result == 1:
            data = True
        else:
            raise ValueError
    except ValueError:
        pass
    finally:
        return data


def delete_user(env, user_id):
    """
    :param env:
    :param user_id:
    :return:
    """
    data = False
    try:
        mysql_manager = MysqlManager(env)
        session = mysql_manager.connect_db()
        db_session = session()
        result = db_session.query(User).filter(User.user_id == user_id).delete()
        db_session.commit()
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
    data = None
    try:
        user = User(user_id=user_id,
                    password=password,
                    username=username,
                    email=email,
                    create_time=create_time)
        mysql_manager = MysqlManager(env)
        session = mysql_manager.connect_db()
        db_session = session()
        db_session.add(user)
        db_session.commit()
        result = get_user(env, user_id)
        if result:
            data = result
        else:
            raise ValueError
    except ValueError:
        pass
    finally:
        return data
