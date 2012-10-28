import sys

from base import Base as Settings


class Development(Settings):
    # Default / Debug Settings
    DEBUG = True
    INTERNAL_IPS = ('127.0.0.1',)

    # Static Media Settings
    if len(sys.argv) > 1 and sys.argv[1] == 'collectstatic':
        STATIC_URL = '//aidoru.s3.amazonaws.com/'
        STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
        AWS_STORAGE_BUCKET_NAME = 'aidoru'

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
