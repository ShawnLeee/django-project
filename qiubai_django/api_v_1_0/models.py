# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from managers import UserManager
from django.db import models
from django.conf import settings
from uuid import uuid4
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from django.contrib.auth.models import AbstractUser


# class V2User(AbstractUser):
#     email = models.EmailField('email address', unique=True, db_index=True)
#     joined = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'

#     def __unicode__(self):
#         return self.email

class QBComment(models.Model):
    comment_id = models.CharField(primary_key=True, max_length=32)
    user = models.ForeignKey('QBUser', models.DO_NOTHING, blank=True, null=True)
    post = models.ForeignKey('QBPost', models.DO_NOTHING, blank=True, null=True)
    comment_text = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)

    def to_dict(self):
        comment_dict = {
            'comment_id': self.comment_id,
            'comment_text': self.comment_text,
            'created_time': str(self.created_time),
            'floor': self.floor,
            'user': self.user.to_dict(),
            'post': self.post.to_dict(),
        }
        return comment_dict


class QBPost(models.Model):
    post_id = models.CharField(primary_key=True, max_length=32)
    user = models.ForeignKey('QBUser',  models.DO_NOTHING, to_field='user_id', blank=False, null=False)
    post_text = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    like_count = models.IntegerField(blank=True, null=True)
    comment_count = models.IntegerField(blank=True, null=True)

    def to_dict(self):

        pics = QBPostPic.objects.filter(post_id=self.post_id)

        pic_urls = []
        for pic in pics:
            pic_urls.append(pic.server_url())

        post_dict = {
            'post_id': self.post_id,
            'user': self.user.to_dict(),
            'post_text': self.post_text,
            'created_time': str(self.created_time),
            'like_count': self.like_count,
            'comment_count': self.comment_count,
            'pics': pic_urls
        }
        return post_dict

    @staticmethod
    def new_post_with(post_text=None, user_id=None):
        post = QBPost()
        post.post_id = uuid4().hex
        post.user_id = user_id
        post.post_text = post_text

        return post


class QBPostPic(models.Model):
    pic_id = models.CharField(primary_key=True, max_length=32)
    post = models.ForeignKey('QBPost', models.DO_NOTHING, blank=True, null=True)
    pic_url = models.CharField(null=False,max_length=64)

    def server_url(self):
        if settings.DEBUG:
            return settings.TES_SERVER_BASE + self.pic_url
        else:
            return settings.PRO_SERVER_BASE + self.pic_url

class QBUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(primary_key=True, max_length=32)
    user_name = models.CharField(max_length=40, blank=True, null=True, unique=True)
    article_count = models.IntegerField(blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    follers_count = models.IntegerField(blank=True, null=True)
    friends_count = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    def get_short_name(self):
        return self.user_name

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = []


    def to_dict(self):
        user_dict = {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'article_count': self.article_count,
            'avatar': self.avatar,
            'friends_count': self.friends_count,
            'follers_count': self.follers_count,
            'gender': self.gender,
        }
        return user_dict


class Roles(models.Model):
    name = models.CharField(unique=True, max_length=64, blank=True, null=True)
    default = models.IntegerField(blank=True, null=True)
    permissions = models.IntegerField(blank=True, null=True)

