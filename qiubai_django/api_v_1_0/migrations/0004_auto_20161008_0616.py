# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-08 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v_1_0', '0003_qbpost_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qbcomment',
            name='floor',
            field=models.IntegerField(blank=True, null=True, verbose_name='Server URL'),
        ),
    ]
