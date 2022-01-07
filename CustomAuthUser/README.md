# Custom User (Django app)

### To Install
in `settings.py`:
```python
INSTALLED_APPS = [
    ...
    'user', # add to installed apps
    ...
]

AUTH_USER_MODEL = 'user.User'
```

> Only one view to test the model has been implemented.

ref: [Creating a Custom User Model in Django [https://testdriven.io/]](https://testdriven.io/blog/django-custom-user-model/)