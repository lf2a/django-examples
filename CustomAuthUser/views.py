# Django
from django.shortcuts import render

# local Django
from .models import User


def info(request):
    '''
    return a list of users - test
    '''
    users = User.objects.all()

    return render(
        request=request,
        template_name='info.html',
        context={
            'users': users
        }
    )
