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
