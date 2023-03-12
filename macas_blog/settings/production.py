from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
CSRF_TRUSTED_ORIGINS = ['https://*.macas.tech','https://macas.tech','https://*.127.0.0.1','http://206.189.153.198']
ALLOWED_HOSTS = ['https://*.macas.tech', 'https://macas.tech', 'https://*.127.0.0.1', '206.189.153.198']
USE_X_FORWARDED_PORT = True