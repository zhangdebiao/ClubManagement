# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u793e\u56e2\u540d\u79f0')),
                ('price', models.IntegerField(verbose_name='\u793e\u56e2\u4eba\u6570')),
                ('author', models.CharField(max_length=128, verbose_name='\u793e\u957f')),
                ('publish_date', models.DateField(verbose_name='\u793e\u56e2\u6210\u7acb\u65e5\u671f')),
                ('category', models.CharField(max_length=128, verbose_name='\u793e\u56e2\u7c7b\u522b')),
                ('detail', models.CharField(max_length=255, verbose_name='\u793e\u56e2\u63cf\u8ff0')),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'management_book',
                'verbose_name_plural': '\u793e\u56e2',
            },
        ),
        migrations.CreateModel(
            name='club_zixun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aid', models.IntegerField(default=0)),
                ('activity_name', models.CharField(max_length=50, verbose_name='\u6d3b\u52a8\u540d\u79f0')),
                ('activity_describe', models.CharField(max_length=200, verbose_name='\u6d3b\u52a8\u63cf\u8ff0')),
                ('activity_person', models.IntegerField(verbose_name='\u6d3b\u52a8\u4eba\u6570')),
                ('activity_img', models.CharField(max_length=255, verbose_name='\u6d3b\u52a8\u56fe\u7247')),
            ],
            options={
                'db_table': 'club_zixun',
                'verbose_name': '\u6d3b\u52a8\u8d44\u8baf',
            },
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u56fe\u7247\u540d\u79f0')),
                ('description', models.TextField(verbose_name='\u56fe\u7247\u63cf\u8ff0')),
                ('img', models.ImageField(upload_to='image/%Y/%m/%d/', verbose_name='\u4e0a\u4f20\u56fe\u7247')),
                ('book', models.ForeignKey(verbose_name='\u6240\u5c5e\u793e\u56e2', to='management.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Myadmin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20, verbose_name='\u8d26\u53f7')),
                ('password', models.CharField(max_length=20, verbose_name='\u5bc6\u7801')),
                ('name', models.CharField(max_length=10, verbose_name='\u771f\u5b9e\u59d3\u540d')),
                ('email', models.CharField(max_length=30, verbose_name='\u90ae\u7bb1')),
            ],
            options={
                'db_table': 'myadmin',
                'verbose_name': '\u540e\u53f0\u7528\u6237',
            },
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.IntegerField(default=0, max_length=11)),
                ('nickname', models.CharField(max_length=16)),
                ('permission', models.IntegerField(default=1)),
                ('user_state', models.IntegerField(default=1)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'management_myuser',
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
    ]
