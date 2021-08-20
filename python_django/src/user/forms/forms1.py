#! /user/bin/env python
# -*- coding:utf-8 -*-


def is_empty(data):
    if not data or type(data) is not dict:
        raise KeyError
    else:
        for v in data.values():
            if v == '':
                raise KeyError
