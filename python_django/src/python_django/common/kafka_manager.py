#! /user1/bin/env python
# -*- coding:utf-8 -*-

from pykafka import KafkaClient


class KafkaManager(object):

    def __init__(self, hosts, topic):
        self.__hosts = hosts
        self.__topic = topic
        self.__conn = None

    def _connect(self):
        self.__conn = KafkaClient(hosts=self.__hosts)

    def _set_topic(self, topic):
        self._connect()
        self.__topic = self.__conn.topics[topic.encode()]

    def set_topic(self, topic):
        """
        设置topic
        :param topic:
        :return:
        """
        self._set_topic(topic)

    def get_topics(self):
        """
        获取当前所有topic
        :return:
        """
        return self.__conn.topics

    def get_topic(self):
        """
        获取当前topic
        :return:
        """
        return self.__topic

    def producer(self):
        """
        生产者对象
        :return:
        """
        with self.__topic.get_producer(delivery_reports=True) as kafka_producer:
            next_data = ''
            while True:
                if next_data:
                    kafka_producer.produce(str(next_data).encode())
                next_data = yield True

    def send_data(self, data):
        """
        发送数据
        :param data:
        :return:
        """
        kafka_client = self.producer()
        next(kafka_client)
        for i in data:
            kafka_client.send(i)
