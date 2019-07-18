from django.shortcuts import render


def homepage(request):
    return render(request, "homepage.html")


def register(request):
    return render(request, "register.html")
