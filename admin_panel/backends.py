from django.contrib.auth.backends import BaseBackend
import requests

class MyAuthBackend(BaseBackend):
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        response = requests.post('https://api-sxm-test.fly.dev/auth/login', data={'username': username, 'password': password})
        if response.status_code == 200:
            # ...
            pass
        return None

    def get_user(self, user_id):
        try:
            # ...
            pass
        except User.DoesNotExist:
            return None

class JWTAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        response = requests.post('https://api-sxm-test.fly.dev/auth/login', data={'username': username, 'password': password})
        if response.status_code == 200:
            # ...
            pass
        return None

    def get_user(self, user_id):
        try:
            # ...
            pass
        except User.DoesNotExist:
            return None