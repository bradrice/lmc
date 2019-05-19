from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c1=mbs2t*!^omg&i0xfo_=mle)%_oegt-&@gn)vx5cs0foe%l9'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*', '0.0.0.0:8080'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
