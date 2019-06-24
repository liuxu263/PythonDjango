from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User
from django.contrib.auth.decorators import login_required


# @login_required(login_url='/login/')
def login(request):
    try:
        userName = request.POST['usr']
        userPwd = request.POST['pwd']
        user = auth.authenticate(username=userName, password=userPwd)
        if user is not None:
            auth.login(request, user)
            return redirect('/check/')
        else:
            return render(request, 'myapp1/login.html', {'msg': '用户名或密码不正确'})
    except:
        return render(request, 'myapp1/login.html', {'msg': None})
