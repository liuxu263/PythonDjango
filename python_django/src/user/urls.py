# coding:utf-8


from django.urls import path
from django.conf.urls import url
from .views import views

urlpatterns = [
    url(r'^session/', views.session),
    url(r'^user/(?P<user_id>\w+)/$', views.user)

]
