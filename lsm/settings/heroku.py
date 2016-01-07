from lsm.settings.base import *

import dj_database_url

DATABASES = {'default': dj_database_url.config(default=get_env('DATABASE_URL'))}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
