# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 17:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_v_1_0', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QBComment',
            fields=[
                ('comment_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('comment_text', models.TextField(blank=True, null=True)),
                ('created_time', models.DateTimeField(blank=True, null=True)),
                ('floor', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QBPost',
            fields=[
                ('post_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('post_text', models.TextField(blank=True, null=True)),
                ('created_time', models.DateTimeField(blank=True, null=True)),
                ('like_count', models.IntegerField(blank=True, null=True)),
                ('comment_count', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QBUser',
            fields=[
                ('user_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, max_length=40, null=True)),
                ('article_count', models.IntegerField(blank=True, null=True)),
                ('avatar', models.CharField(blank=True, max_length=255, null=True)),
                ('password_hash', models.CharField(blank=True, max_length=128, null=True)),
                ('follers_count', models.IntegerField(blank=True, null=True)),
                ('friends_count', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True)),
                ('token', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('default', models.IntegerField(blank=True, null=True)),
                ('permissions', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='QUser',
        ),
        migrations.AddField(
            model_name='qbpost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api_v_1_0.QBUser'),
        ),
        migrations.AddField(
            model_name='qbcomment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_v_1_0.QBPost'),
        ),
        migrations.AddField(
            model_name='qbcomment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_v_1_0.QBUser'),
        ),
    ]
