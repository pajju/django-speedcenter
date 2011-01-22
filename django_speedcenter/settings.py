from speedcenter.settings import *

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME':'django_speedcenter',
            'USER': 'django_speedcenter',
            'PASSWORD': 'django_speedcenter',
            }
        }

INTERNAL_IPS = ('127.0.0.1', )

CACHE_BACKEND = 'memcached://127.0.0.1:11211'

TEMPLATE_DIRS = (
        os.path.join(os.path.dirname(__file__), 'templates'),
        os.path.join(os.path.dirname(__file__), '..', 'codespeed', 'speedcenter', 'templates'),
        )

ROOT_URLCONF = 'django_speedcenter.urls'
