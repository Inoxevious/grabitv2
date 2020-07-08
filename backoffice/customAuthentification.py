# -*-coding:utf-8 -*-
from django.contrib.auth.models import User
from .libs import *
from .models import User
class customAuthentification(object):
    """
    Use the login name and a hash of the password. For example:
    """
    def authenticate(self, username=None, password=None):
        if username:
            try:
                user = User.objects.get(username=username)
                encoder = SHA256PasswordHasher()
                if SHA256PasswordHasher.verify(encoder,password,user.password):
                    return user
                else:
                    return  None
            except User.DoesNotExist:
                return None
        return None
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None