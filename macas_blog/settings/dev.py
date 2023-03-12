from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-byd+#(-wq+-@qu#$0zy)lh_k+79tm*mmzw^g$w(4d#3_9=!6gy"

# SECURITY WARNING: define the correct hosts in production!
CSRF_TRUSTED_ORIGINS = ['https://*.macas.tech','https://macas.tech','https://*.127.0.0.1','http://206.189.153.198']
ALLOWED_HOSTS = ['https://*.macas.tech', 'https://macas.tech', 'https://*.127.0.0.1', '206.189.153.198']
USE_X_FORWARDED_PORT = True
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

try:
    from .local import *
except ImportError:
    pass
