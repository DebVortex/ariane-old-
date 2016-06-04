import os
from configurations import values


class Databases(object):
    """Settings for PostgreSQL databases."""

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('PG_NAME', 'ariane'),
            'USER': os.environ.get('PG_USER', 'ariane'),
            'PASSWORD': os.environ.get('PG_PASSWORD', 'ariane'),
            'HOST': os.environ.get('PG_HOST', '127.0.0.1'),
            'PORT': os.environ.get('PG_PORT')
        }
    }

    # Number of seconds database connections should persist for
    DATABASES['default']['CONN_MAX_AGE'] = values.IntegerValue(600, environ_prefix='',
        environ_name='DEFAULT_CONN_MAX_AGE')
