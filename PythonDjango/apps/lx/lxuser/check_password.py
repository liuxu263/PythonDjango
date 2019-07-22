from django.shortcuts import render


def check_password(password, password1):
    msg = 200
    if check_password_length(password) is True:
        msg = "密码过短"
    return msg


def check_password_length(password):
    if len(password) <= 8:
        return True
