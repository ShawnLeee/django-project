# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AlembicVersion(models.Model):
    version_num = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'alembic_version'


class CommentsT(models.Model):
    comment_id = models.CharField(primary_key=True, max_length=255)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    post = models.ForeignKey('PostsT', models.DO_NOTHING, blank=True, null=True)
    comment_text = models.TextField(blank=True, null=True)
    floor = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments_t'


class LsCommentsT(models.Model):
    comment_id = models.CharField(primary_key=True, max_length=32)
    user = models.ForeignKey('LsusersT', models.DO_NOTHING, blank=True, null=True)
    post = models.ForeignKey('LsPost', models.DO_NOTHING, blank=True, null=True)
    comment_text = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ls_comments_t'


class LsPost(models.Model):
    post_id = models.CharField(primary_key=True, max_length=32)
    user = models.ForeignKey('LsusersT', models.DO_NOTHING, blank=True, null=True)
    post_text = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    like_count = models.IntegerField(blank=True, null=True)
    comment_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ls_post'


class LsusersT(models.Model):
    user_id = models.CharField(primary_key=True, max_length=32)
    user_name = models.CharField(max_length=40, blank=True, null=True)
    article_count = models.IntegerField(blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    password_hash = models.CharField(max_length=128, blank=True, null=True)
    follers_count = models.IntegerField(blank=True, null=True)
    friends_count = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lsusers_t'


class Posts(models.Model):
    body = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts'


class PostsT(models.Model):
    post_id = models.CharField(primary_key=True, max_length=255)
    user = models.ForeignKey('UsersT', models.DO_NOTHING, blank=True, null=True)
    post_text = models.TextField(blank=True, null=True)
    like_count = models.IntegerField(blank=True, null=True)
    comment_count = models.IntegerField(blank=True, null=True)
    created_time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts_t'


class Roles(models.Model):
    name = models.CharField(unique=True, max_length=64, blank=True, null=True)
    default = models.IntegerField(blank=True, null=True)
    permissions = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Users(models.Model):
    email = models.CharField(unique=True, max_length=64, blank=True, null=True)
    username = models.CharField(unique=True, max_length=64, blank=True, null=True)
    role = models.ForeignKey(Roles, models.DO_NOTHING, blank=True, null=True)
    password_hash = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsersT(models.Model):
    user_id = models.CharField(primary_key=True, max_length=255)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    author_url = models.CharField(max_length=255, blank=True, null=True)
    post_count = models.IntegerField(blank=True, default=0, null=True)

    class Meta:
        managed = False
        db_table = 'users_t'
