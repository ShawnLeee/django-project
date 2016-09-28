# encoding: utf-8
from __future__ import unicode_literals
from werkzeug.security import generate_password_hash, check_password_hash

from django.db import models

# Create your models here.

class LSUser(models.Model):

    user_name = models.CharField(max_length=128)
    password_hash = models.CharField(max_length=128)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def user_with(user_name, password):
        t_user = LSUser(user_name=user_name, password=password)
        return t_user


#
# class Article(object):
#     pass
# # def save2db(self):
# #         self.save()
#
#
# class Comment(object):
#     pass
#     # def save2db(self):
#         #查询这条评论的用户是否存在,先插入用户



