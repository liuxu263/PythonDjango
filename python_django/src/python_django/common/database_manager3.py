#! /user/bin/env python
# -*- coding:utf-8 -*-

import os
import yaml
import pymysql
from yaml.loader import FullLoader

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class MysqlManager(object):

    def __init__(self, env, service):
        base_file = os.path.abspath(
            os.path.dirname(os.path.dirname(os.path.dirname((os.path.dirname(os.path.dirname(__file__)))))))
        with open(base_file + '/config/' + service + '/db') as file:
            db = yaml.load(file.read(), Loader=FullLoader)
        self.__database_name = db[env]["db"]
        self.__db_user = db[env]["user"]
        self.__db_password = db[env]["password"]
        self.__host = db[env]["host"]
        self.__port = db[env]["port"]
        self.__engine = None
        self.__session = None

    def connect_db(self):
        params = {
            "database": self.__database_name,
            "user": self.__db_user,
            "password": self.__db_password,
            "host": self.__host,
            "port": self.__port
        }
        connect = "mysql+pymysql://%s:%s@%s:%d/%s?charset=utf8" % (
            params["user"],
            params["password"],
            params["host"],
            int(params["port"]),
            params["database"])
        self.__engine = create_engine(connect)
        self.__session = sessionmaker(bind=self.__engine)
        return self.__session

    def close_db(self):
        self.__session.close()
        self.__engine.close()
