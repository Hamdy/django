from typing import Any
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http import HttpRequest

from .models import User

class AuthBackend(BaseBackend):
    def get_user(self, user_id: int) -> AbstractBaseUser | None:
        try:
            return User.objects.get(user_id)
        except User.DoesNotExist:
            ...

    def authenticate(self, request: HttpRequest, username: str | None , password: str, **kwargs: Any) -> AbstractBaseUser | None:
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user            
        except User.DoesNotExist:
            ...
