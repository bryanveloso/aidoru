# -*- coding: utf-8 -*-
import datetime
import os

from os.path import abspath, basename, dirname, join, normpath
from sys import path

from configurations import Settings


class Base(Settings):
    # Path Configuration
    DJANGO_ROOT = dirname(dirname(abspath(__file__)))
    SITE_ROOT = dirname(DJANGO_ROOT)
    SITE_NAME = basename(DJANGO_ROOT)

    # Add our project to our pythonpath, this way we don't need to type our
    # project name in our dotted import paths:
    path.append(DJANGO_ROOT)

    # Default / Debug Settings
    ROOT_URLCONF = '%s.urls' % SITE_NAME
    SITE_ID = 1
    TEMPLATE_DEBUG = Settings.DEBUG

    # Emails
    ADMINS = [('Bryan Veloso', 'bryan@hello-ranking.com')]
    MANAGERS = [('Jennifer Verduzco', 'jen@hello-ranking.com')]

    # Localization
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    # Template Settings
    TEMPLATE_DIRS = (normpath(join(DJANGO_ROOT, 'templates')),)
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    # Installed Applications
    DJANGO_APPLICATIONS = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.staticfiles'
    ]
    COMPONENTS = [
        'modules.images',
        'modules.people'
    ]
    PLUGINS = [
        'gunicorn',
        'taggit'
    ]
    ADMINISTRATION = [
        'grappelli',
        'django.contrib.admin'
    ]
    INSTALLED_APPS = DJANGO_APPLICATIONS + COMPONENTS + PLUGINS + ADMINISTRATION

    # Python dotted path to the WSGI application used by Django's runserver.
    WSGI_APPLICATION = 'wsgi.application'

    # Logging
    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }

    # Make this unique, and don't share it with anybody.
    SECRET_KEY = 'vng^zp@j9sf(_i=gvgtn6vj1qivo)ke#ft42o1wc@tur+1pl#o'

    # Media Settings
    MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))
    MEDIA_URL = '/media/'

    # Static Media Settings
    STATIC_ROOT = normpath(join(SITE_ROOT, 'static'))
    STATIC_URL = '/static/'

    # Django Grappelli
    GRAPPELLI_ADMIN_TITLE = 'Aidoru'
