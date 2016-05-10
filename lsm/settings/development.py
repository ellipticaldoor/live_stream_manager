from lsm.settings.base import *

DEBUG = True

# INSTALLED_APPS += (
# 	'debug_toolbar',
# )
#
# MIDDLEWARE_CLASSES += (
# 	'debug_toolbar.middleware.DebugToolbarMiddleware',
# )
#
# DEBUG_TOOLBAR_CONFIG = {
# 	'JQUERY_URL': '/s/js/lib/jquery_2.1.3.min.js',
# }

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
