import os
import sys

from base import Base as Settings


class Development(Settings):
    # Default / Debug Settings
    DEBUG = True
    INTERNAL_IPS = ('127.0.0.1',)

    # Database Settings
    DATABASES = {
        'default': {
            'HOST': '127.0.0.1',
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'aidoru_development',
            'USER': 'Bryan',
            'PASSWORD': ''
        }
    }
