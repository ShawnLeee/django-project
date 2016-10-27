from api_v_1_0.models import QBUser


class MyCustomBackend:
	def authenticate(self, uname=None, password=None):
		try:
			user = QBUser.objects.get(user_name=uname)
		except QBUser.DoesNotExist:
			pass
		else:
			if user.check_password():
				return user
			else:
				return None

	def get_user(self, user_id):
		try:
			return QBUser.objects.get(user_id=user_id)
		except QBUser.DoesNotExist:
			return None
