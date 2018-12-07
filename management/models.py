#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    user = models.OneToOneField(User)
    uid = models.IntegerField(max_length=11, default=0, verbose_name='所属社团')
    nickname = models.CharField(max_length=16, verbose_name='账号')
    permission = models.IntegerField(default=1, verbose_name='用户权限')
    user_state = models.IntegerField(default=1, verbose_name='状态')

    class Meta:
        db_table = 'management_myuser'
        verbose_name = '前台用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username



class Club(models.Model):
    name = models.CharField(max_length=128, verbose_name='社团名称')
    price = models.IntegerField(verbose_name='社团人数')
    author = models.CharField(max_length=128, verbose_name='社长')
    publish_date = models.DateField(verbose_name='社团成立日期')
    category = models.CharField(max_length=128, verbose_name='社团类别')
    detail = models.CharField(max_length=255, verbose_name='社团描述')

    class Meta:
        db_table = 'management_book'
        verbose_name = "社团"
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name



class Img(models.Model):
    name = models.CharField(max_length=128, verbose_name='图片名称')
    description = models.TextField(verbose_name='图片描述')
    img = models.ImageField(upload_to='image/%Y/%m/%d/', verbose_name='上传图片')
    book = models.ForeignKey(Club, verbose_name='所属社团')

    class META:
        db_table = 'management_img'
        verbose_name = '社团图片'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return self.name



class club_zixun(models.Model):
    aid = models.IntegerField(default=0)
    activity_name = models.CharField(max_length=50, verbose_name='活动名称')
    activity_describe = models.CharField(max_length=200, verbose_name='活动描述')
    activity_person = models.IntegerField(verbose_name='活动人数')
    activity_img = models.CharField(max_length=255, verbose_name='活动图片')

    class Meta:
        db_table = 'club_zixun'
        verbose_name = '活动资讯'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.activity_name




# 后台管理员表
class Myadmin(models.Model):
    username = models.CharField(max_length=20, verbose_name='账号')
    password = models.CharField(max_length=20, verbose_name='密码')
    name = models.CharField(max_length=10, verbose_name='真实姓名')
    email = models.CharField(max_length=30, verbose_name='邮箱')

    class Meta:
        db_table = 'myadmin'
        verbose_name = '后台用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

