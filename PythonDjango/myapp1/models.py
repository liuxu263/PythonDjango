from django.db import models


class Test(models.Model):
    # userid = models.CharField('用户编号', max_length=20, primary_key=True)
    # id = models.AutoField(primary_key=True, blank=True, null=True)
    account = models.CharField("登录账号", max_length=50, blank=True, unique=True)
    name = models.CharField("姓名", max_length=20)
    sex = models.CharField("性别", max_length=10)
    # birthday = models.DateField('生日')
    # age = models.IntegerField("年龄")
    # email = models.EmailField('电子信箱', blank=True)
    # province = models.CharField("省", max_length=10)
    # city = models.CharField("市", max_length=10)
    # county = models.CharField("县", max_length=10)
    # nation = models.CharField("民族", max_length=10)
    # phone = models.CharField("电话号", max_length=20, unique=True)
    # registerTime = models.DateTimeField("注册时间", auto_now=True)


class Test1(models.Model):
    # userid = models.CharField('用户编号', max_length=20, primary_key=True)
    # id = models.AutoField(primary_key=True, blank=True, null=True)
    account = models.CharField("登录账号", max_length=50, blank=True, unique=True)
    name = models.CharField("姓名", max_length=20)
    sex = models.CharField("性别", max_length=10)
    # birthday = models.DateField('生日')
    # age = models.IntegerField("年龄")
    # email = models.EmailField('电子信箱', blank=True)
    # province = models.CharField("省", max_length=10)
    # city = models.CharField("市", max_length=10)
    # county = models.CharField("县", max_length=10)
    # nation = models.CharField("民族", max_length=10)
    # phone = models.CharField("电话号", max_length=20, unique=True)
    # registerTime = models.DateTimeField("注册时间", auto_now=True)
