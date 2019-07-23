#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

''

__author__ = 'lx'

from django.shortcuts import render
from .check_nickname import *
from .check_password import *
from .check_phone import *
from .check_email import *
from _md5 import md5


def register(request):
    try:
        post = request.POST
        nickname = post.get('nickname')
        if check_nickname_diff(nickname) is True:
            return render(request, 'register.html', {'msg': '昵称已经存在'})
        name = post.get('name')
        password = post.get('pwd1')
        password1 = post.get('pwd2')
        if check_password_diff(password, password1) is not True:
            return render(request, 'register.html', {'msg': '两次密码不同'})
        if check_password_length(password) is not True:
            return render(request, 'register.html', {'msg': '密码长度过短'})
        password = md5(password)
        sex = post.get('sex')
        birthday = post.get('birthday')
        age = post.get('age')
        idcard = post.get('IDCard')
        nation = post.get('nation')
        province = post.get('province')
        city = post.get('city')
        county = post.get('county')
        phone = post.get('phone')
        if check_phone_diff(phone) is not True:
            return render(request, 'register.html', {'msg': '电话号已经存在'})
        email = post.get('email')
        if check_email_diff(email) is not True:
            return render(request, 'register.html', {'msg': '邮箱已经存在'})
        user = User(nickname=nickname, name=name, password=password, sex=sex,
                    birthday=birthday, age=age, IDCard=idcard, nation=nation, province=province,
                    city=city, county=county, phone=phone, email=email)
        user.save()
        return render(request, 'homepage.html', {'msg': "注册成功"})
    except:
        return render(request, 'register.html', {'msg': '注册失败'})
