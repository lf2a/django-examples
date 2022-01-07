# Django
from django.contrib.auth.forms import (
    UserCreationForm as CreationForm,
    UserChangeForm as ChangeForm
)

# local Django
from .models import User


class UserCreationForm(CreationForm):
    class Meta(CreationForm):
        model = User
        fields = ('avatar', 'username', 'email',)


class UserChangeForm(ChangeForm):
    class Meta:
        model = User
        fields = ('avatar', 'username', 'email',)
