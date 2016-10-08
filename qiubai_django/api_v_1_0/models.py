# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


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
    img_url = models.URLField("Server URL", blank=True)

    def to_dict(self):
        post_dict = {
            'post_id': self.post_id,
            'user': self.user.to_dict(),
            'post_text': self.post_text,
            'created_time': str(self.created_time),
            'like_count': self.like_count,
            'comment_count': self.comment_count,
        }
        return post_dict


class QBUser(models.Model):
    user_id = models.CharField(primary_key=True, max_length=32)
    user_name = models.CharField(max_length=40, blank=True, null=True)
    article_count = models.IntegerField(blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    password_hash = models.CharField(max_length=128, blank=True, null=True)
    follers_count = models.IntegerField(blank=True, null=True)
    friends_count = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)

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

