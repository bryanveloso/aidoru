import os
import sys
import urlparse

from base import Base as Settings


class Production(Settings):
    DEBUG = True

    # Secret Key
    if hasattr(os.environ, 'SECUREKEY_CRIMSON_KEY'):
        SECRET_KEY = os.environ['SECUREKEY_CRIMSON_KEY'].split(',')[0]

    # Heroku =================================================================
    # Database Settings
    def DATABASES(self):
        from dj_database_url import config
        return {'default': config(default='postgres://localhost')}

    # Cache Settings
    try:
        urlparse.uses_netloc.append('redis')
        if 'REDISTOGO_URL' in os.environ:
            url = urlparse.urlparse(os.environ['REDISTOGO_URL'])
            REDIS_BACKENDS = {
                'default': {
                    'db': 0,
                    'host': url.hostname,
                    'password': url.password,
                    'port': url.port
                }
            }
            Settings.CACHES['default'] = {
                'BACKEND': 'redis_cache.RedisCache',
                'LOCATION': '%s:%d' % (REDIS_BACKENDS['default']['host'], REDIS_BACKENDS['default']['port']),
                'KEY_PREFIX': 'ranking.production',
                'OPTIONS': {
                    'DB': REDIS_BACKENDS['default']['db'],
                    'PASSWORD': REDIS_BACKENDS['default']['password'],
                }
            }
    except:
        print 'Unexpected error:', sys.exc_info()
