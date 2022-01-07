# Django
from django.urls import path

# local Django
from .views import info

urlpatterns = [
    path('', info, name='user_info'),
]
