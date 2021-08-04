#! /user/bin/env python
# -*- coding:utf-8 -*-


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class MysqlManager(object):

    def __init__(self, database_name, db_user, db_password, host='localhost', port=3306):
        self.__database_name = database_name
        self.__db_user = db_user
        self.__db_password = db_password
        self.__host = host
        self.__port = port
        self.__engine = None
        self.__session = None

    def _connect_db(self):
        params = {
            "database": self.__database_name,
            "user": self.__db_user,
            "password": self.__db_password,
            "host": self.__host,
            "port": self.__port
        }
        connect = 'mysql+pymysql://s%:s%@s%:s%/s%', (
            params["user"],
            params["password"],
            params["host"],
            params["port"],
            params["database"])
        self.__engine = create_engine(connect)
        self.__session = sessionmaker(bind=self.__engine)

    def _close_db(self):
        self.__session.close()
        self.__engine.close()


if __name__ == '__main__':
    db = MysqlManager("lx", "root", "liuxu263", "localhost", 3306)
    print(dir(db))
