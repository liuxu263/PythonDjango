from django.db import models


class User(models.Model):
    userid = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    birthday = models.DateField()
    age = models.IntegerField()
    province = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    county = models.CharField(max_length=10)
    nation = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)



