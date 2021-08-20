#! /user1/bin/env python
# -*- coding:utf-8 -*-


import os
import time

if __name__ == '__main__':
    base_file = os.path.abspath(os.path.dirname(__file__))
    # mode1
    # status = os.system("sh " + base_file + "./bin/python_django/sh/start_server")
    # if status != 0:
    #     print("服务器启动异常")

    # mode2
    try:
        pid = ''.join(os.popen("lsof -i:8000 | awk '{print $2}' | sed -n '2p'").read())[:-1]
        if pid != '':
            result = os.system("kill -9 " + str(pid))
            print(str(pid))
            if result == 0:
                print("杀死进程" + str(pid) + "成功")
            else:
                print("杀死进程" + str(pid) + "失败")
        else:
            print("端口未被占用")
    except IOError:
        pass
    finally:
        time.sleep(2)
        status = os.system("python " + base_file + "/python_django/src/manage.py runserver")
        if status != 0:
            print("服务器启动异常")
