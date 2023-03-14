from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
CSRF_TRUSTED_ORIGINS = ['https://*.macas.tech','https://macas.tech','https://*.127.0.0.1','http://206.189.153.198']
ALLOWED_HOSTS = ['https://*.macas.tech', 'https://macas.tech', 'www.macas.tech', 'macas.tech', 'https://*.127.0.0.1',
                 '206.189.153.198']
USE_X_FORWARDED_PORT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
