# coding:utf-8


import os
import MySQLdb
import yaml
from yaml.loader import FullLoader


class MysqlManager(object):

    def __init__(self, env):
        """
        :param env:
        """
        base_file = os.path.abspath(
            os.path.dirname(os.path.dirname(os.path.dirname((os.path.dirname(os.path.dirname(__file__)))))))
        with open(base_file + '/python_django/src/user/config/db') as file:
            db = yaml.load(file.read(), Loader=FullLoader)
        self.__database_name = db[env]["db"]
        self.__db_user = db[env]["user"]
        self.__db_password = db[env]["password"]
        self.__host = db[env]["host"]
        self.__port = db[env]["port"]
        self.__connect = None
        self.__cursor = None

    def _connect_db(self):
        params = {
            "database": self.__database_name,
            "user": self.__db_user,
            "password": self.__db_password,
            "host": self.__host,
            "port": self.__port
        }
        self.__connect = MySQLdb.connect(**params)
        self.__cursor = self.__connect.cursor(MySQLdb.cursors.DictCursor)

    def _close_db(self):
        self.__cursor.close()
        self.__connect.close()

    def cud(self, sql, params):
        """
        :param sql: str
        :param params: tuple
        :return:
        """
        self._connect_db()
        result = None
        try:
            self.__cursor.execute(sql, params)
            result = self.__cursor.rowcount
            self.__connect.commit()
        except Exception:
            self.__connect.rollback()
            raise KeyError
        finally:
            self._close_db()
            return result

    def select(self, sql, params=None):
        """
        :param sql: str
        :param params: tuple
        :return:
        """
        self._connect_db()
        result = None
        try:
            self.__cursor.execute(sql, params)
            result = self.__cursor.fetchall()
        except Exception:
            raise KeyError
        finally:
            self._close_db()
            return result
