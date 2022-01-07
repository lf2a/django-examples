# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA

# local Django
from .form import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(UA):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = (
        'username',
        'email',
        'is_staff',
        'is_active'
    )
    list_filter = (
        'username',
        'email',
        'is_staff',
        'is_active'
    )

    fieldsets = (
        (
            None, {
                'fields': ('email', 'password')
            }),
        (
            'Permissions', {
                'fields': ('is_staff', 'is_active')
            }
        ),
    )

    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'avatar',
                    'username',
                    'email',
                    'password1',
                    'password2',
                    'is_staff',
                    'is_active'
                )
            }
        ),
    )

    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)
