# coding:utf-8


import redis


class RedisManager(object):

    def __init__(self, host="localhost", password=None, port=6379):
        self._host = host
        self._port = port
        self._password = password
        self.conn_pool = None
        self.conn = None

    def connect(self):
        self.conn_pool = redis.ConnectionPool(host=self._host, port=self._port)
        self.conn = redis.Redis(connection_pool=self.conn_pool)
        return self.conn
