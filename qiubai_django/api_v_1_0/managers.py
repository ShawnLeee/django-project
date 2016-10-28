from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
	user_in_migrations = True

	def _create_user(self, user_name, password, **extra_fields):
		"""
		Creates and Saves a User with the given email and password
		"""
		if not user_name:
			raise ValueError('The given username must be set')
		# email = self.normalize_email(email)
		user = self.model(user_name=user_name, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, user_name, password=None, **extra_fields):
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(user_name, password, **extra_fields)

	def create_superuser(self, user_name, password, **extra_fields):
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True')

		return self._create_user(user_name, password, **extra_fields)

