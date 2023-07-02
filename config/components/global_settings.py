import os

from django.core.management.utils import get_random_secret_key

DEBUG = os.environ.get('DEBUG', default=False) in ['True', 'true', '1']
SECRET_KEY = os.environ.get('SECRET_KEY', default=get_random_secret_key())
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(', ')
