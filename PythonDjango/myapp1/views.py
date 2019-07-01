#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

''

__author__ = 'lx'

from _md5 import md5

from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Test1


def hoempage(request):
    return render(request, "homepage.html")


def login(request):
    try:
        userName = request.POST['usr']
        userPwd = request.POST['pwd']
        user = auth.authenticate(username=userName, password=userPwd)
        if user is not None:
            auth.login(request, user)
            return redirect('/myapp1/homepage/')
        else:
            return render(request, 'myapp1/login.html', {'msg': '用户名或密码不正确'})
    except:
        return render(request, 'myapp1/login.html', {'msg': None})


def register(request):
    try:
        post = request.POST
        account = post.get('account')
        # if Test.objects.filter(account=account).exists():
        #     return render(request, "myapp1/register.html", {'msg': '账号已存在'})
        # password = post.get('pwd1')
        # p2 = post.get('pwd2')
        # if password != p2:
        #     return render(request, "myapp1/register.html", {'msg': '两次密码不一样'})
        # password = md5(password.encode()).hexdigest()
        # userid = datetime.datetime.now().strftime()
        name = post.get('name')
        sex = post.get('sex')
        birthday = post.get('birthday')
        nation = post.get('nation')
        age = post.get('age')
        province = post.get('province')
        city = post.get('city')
        county = post.get('county')
        phone = post.get('phone')
        email = post.get('email')
        Test1.objects.create(account=account, name=name, sex=sex)
        return render(request, "myapp1/register.html", {'msg': "注册成功"})
    except:
        return render(request, "myapp1/register.html", {'msg': None})
