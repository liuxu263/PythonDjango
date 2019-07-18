from django.shortcuts import render


def register(request):
    re = request.get('register')
    pass
    return render(request, "/lx/register.html")
