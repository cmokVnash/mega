from typing import Any
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# Create your models here.


class UserManager(BaseUserManager):
    def create(self, username, password, **extra_fields: Any) -> Any:
        if not username:
            raise ValueError("Username must be present")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def createsuperuser(self, **kwargs: Any) -> Any:
        return super().create(**kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    username = models.CharField(max_length=30, null=True, blank=True, unique=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(max_length=13, null=True, blank=True, unique=True)

    USERNAME_FIELD = "username"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.username
