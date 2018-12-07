# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='club',
            options={'ordering': ['name'], 'verbose_name': '\u793e\u56e2', 'verbose_name_plural': '\u793e\u56e2'},
        ),
        migrations.AlterModelOptions(
            name='club_zixun',
            options={'verbose_name': '\u6d3b\u52a8\u8d44\u8baf', 'verbose_name_plural': '\u6d3b\u52a8\u8d44\u8baf'},
        ),
        migrations.AlterModelOptions(
            name='myadmin',
            options={'verbose_name': '\u540e\u53f0\u7528\u6237', 'verbose_name_plural': '\u540e\u53f0\u7528\u6237'},
        ),
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name': '\u524d\u53f0\u7528\u6237', 'verbose_name_plural': '\u524d\u53f0\u7528\u6237'},
        ),
        migrations.AlterField(
            model_name='myuser',
            name='nickname',
            field=models.CharField(max_length=16, verbose_name='\u8d26\u53f7'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='permission',
            field=models.IntegerField(default=1, verbose_name='\u7528\u6237\u6743\u9650'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='uid',
            field=models.IntegerField(default=0, max_length=11, verbose_name='\u6240\u5c5e\u793e\u56e2'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='user_state',
            field=models.IntegerField(default=1, verbose_name='\u72b6\u6001'),
        ),
    ]
