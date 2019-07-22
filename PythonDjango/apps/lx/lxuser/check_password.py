from django.shortcuts import render


def check_password(request, password, password1):
    check_password_length(request, password)


def check_password_length(request, password):
    if len(password) <= 8:
        print(len(password))
        return False
