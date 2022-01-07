# Django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

# local Django
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    avatar = models.ImageField(upload_to='avatar', verbose_name='Avatar')
    username = models.CharField(_('Username'), max_length=15, unique=True)
    email = models.EmailField(_('Email Address'), unique=True)
    is_staff = models.BooleanField(default=False, verbose_name='Is Staff')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    date_joined = models.DateTimeField(default=now, verbose_name='Date Joined')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email
