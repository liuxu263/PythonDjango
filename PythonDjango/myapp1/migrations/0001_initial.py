# Generated by Django 2.2.2 on 2019-07-01 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(blank=True, max_length=50, unique=True, verbose_name='登录账号')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('sex', models.CharField(max_length=10, verbose_name='性别')),
            ],
        ),
    ]
