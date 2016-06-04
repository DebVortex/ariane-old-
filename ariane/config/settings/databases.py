import os
from configurations import values


class Databases(object):
    """Settings for PostgreSQL databases."""

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': os.environ.get('PG_USER', 'ariane'),
            'PASSWORD': os.environ.get('PG_PASSWORD', 'ariane'),
        }
    }

    # Number of seconds database connections should persist for
    DATABASES['default']['CONN_MAX_AGE'] = values.IntegerValue(600, environ_prefix='',
        environ_name='DEFAULT_CONN_MAX_AGE')
