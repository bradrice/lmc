from .base import *

DEBUG = False

ALLOWED_HOSTS = [
        'lmc.oh-joy.org',
        'lafayetteumc.net',
        'www.lafayetteumc.net',
        'lafayetteumc.com',
        'www.lafayetteumc.com'
        ]

with open('/usr/local/secret/lmc/secretkey.txt') as f:
    SECRET_KEY = f.read().strip()

    # STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = '/var/www/html/static.lafayetteumc.net/public_html'
# STATIC_URL = '/static/'
STATIC_URL = 'https://static.lafayetteumc.com'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'https://media.lafayetteumc.com'
# MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/html/media.lafayetteumc.net/public_html'

try:
    from .local import *
except ImportError:
    pass

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/www/webapps/lmc/log/django/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
