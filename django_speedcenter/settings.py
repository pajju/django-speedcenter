from speedcenter.settings import *
import speedcenter

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'django_speedcenter',
            'USER': 'django_speedcenter',
            'PASSWORD': 'django_speedcenter',
            }
        }

INTERNAL_IPS = ('127.0.0.1', )

CACHE_BACKEND = 'memcached://127.0.0.1:11211'

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'), ) + TEMPLATE_DIRS

ROOT_URLCONF = 'django_speedcenter.urls'

DEBUG = False
SERVE_STATIC = True

MIDDLEWARE_CLASSES += ('sugar.cache.middleware.HTTPCacheControlMiddleware', )

DEFAULT_HTTP_CACHE_CONTROL = dict(public=True, max_age=864000)
