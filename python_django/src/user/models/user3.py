#! /user/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import INT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    id = Column(INT, primary_key=True)
    user_id = Column(String(20), unique=True)
    password = Column(String(32))
    username = Column(String(16))
    email = Column(String(255))
    create_time = Column(String(30))

    __tablename__ = 'user'
