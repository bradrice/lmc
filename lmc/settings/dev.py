from .base import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c1=mbs2t*!^omg&i0xfo_=mle)%_oegt-&@gn)vx5cs0foe%l9'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*', '0.0.0.0:8080'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = '/var/www/html/static.lafayetteumc.net/public_html'
STATIC_URL = '/static/'
# STATIC_URL = 'https://static.lafayetteumc.com'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = 'https://media.lafayetteumc.com'
MEDIA_URL = '/media/'
# MEDIA_ROOT = '/var/www/html/media.lafayetteumc.net/public_html'

try:
    from .local import *
except ImportError:
    pass
