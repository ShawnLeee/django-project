from api_v_1_0.models import QBUser
from rest_framework import authentication
from rest_framework import exceptions


class MyCustomBackend:
	def authenticate(self, uname=None, password=None):
		try:
			user = QBUser.objects.get(user_name=uname)
		except QBUser.DoesNotExist:
			pass
		# else:
		# 	if user.check_password():
		# 		return user

		return user

	def get_user(self, user_id):
		try:
			return QBUser.objects.get(user_id=user_id)
		except QBUser.DoesNotExist:
			return None

class EAuthentication(authentication.BaseAuthentication):
	def authenticate(self, request):
		pass


class MyBackend(object):
	def authenticate(self, username=None, password=None):
		try:
			user = QBUser.objects.get(user_name=username)
		except QBUser.DoesNotExist:
			pass

		return user

	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None

