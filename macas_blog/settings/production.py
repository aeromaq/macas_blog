from .base import *

DEBUG = True

try:
    from .local import *
except ImportError:
    pass
CSRF_TRUSTED_ORIGINS = ['https://*.macas.tech','https://macas.tech','https://*.127.0.0.1','http://206.189.153.198']
ALLOWED_HOSTS = ['https://*.macas.tech', 'https://macas.tech', 'www.macas.tech', 'macas.tech', '*.127.0.0.1',
                 '206.189.153.198']
USE_X_FORWARDED_PORT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"



AWS_ACCESS_KEY_ID = 'DO003BAK7UJQX7CE3NJC'
AWS_SECRET_ACCESS_KEY = 'QJCHRNtfmsywZQiQhdz2RFhoALGnwVeWZ6HsOJpzdpI'
AWS_STORAGE_BUCKET_NAME = 'macas-tech'
AWS_S3_ENDPOINT_URL = 'https://macas-tech.sgp1.digitaloceanspaces.com'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
AWS_DEFAULT_ACL = 'public-read'
AWS_LOCATION = 'static'
PUBLIC_MEDIA_LOCATION = 'media'
STATIC_URL = "https://%s/%s/" % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)
MEDIA_URL = "https://%s/%s/" % (AWS_S3_ENDPOINT_URL, PUBLIC_MEDIA_LOCATION)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
WAGTAILIMAGES_IMAGE_MODEL = 'utils.CustomImage'
AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_AUTH = False