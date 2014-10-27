import os

from settings.common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ubuntu',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': os.environ["POSTGRES_ADDR"],
        'PORT': os.environ["POSTGRES_PORT"],
    }
}

DATABASES['default']['NAME'] = '{0}'.format(DATABASES['default']['NAME'])