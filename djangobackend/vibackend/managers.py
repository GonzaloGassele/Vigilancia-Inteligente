from django.contrib.auth.models import BaseUserManager
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, username,  email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(username=username)
        user = self.model(email=self.normalize_email(email),)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password,)

        user.is_superuser = True
        user.save()
        return user