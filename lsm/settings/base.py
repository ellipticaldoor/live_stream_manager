import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

from django.core.exceptions import ImproperlyConfigured

def get_env(setting):
	""" Get the environment setting or return exception """
	try:
		return os.environ[setting]
	except KeyError:
		error_msg = 'Set the %s env variable' % setting
		raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_env('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'core',
	'user',
	'panel',
	'timer',
	'tablet',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'lsm.urls'

WSGI_APPLICATION = 'lsm.wsgi.application'

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': get_env('DB_NAME'),
		'USER': get_env('DB_USER'),
		'PASSWORD': get_env('DB_PASSWORD'),
		'HOST': get_env('DB_HOST'),
		'PORT': get_env('DB_PORT'),
	}
}

LANGUAGE_CODE = get_env('LANGUAGE')

TIME_ZONE = 'Atlantic/Canary'

# AUTH_PASSWORD_VALIDATORS = [
# 	{
# 		'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
# 	},
# 	{
# 		'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
# 	},
# 	{
# 		'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
# 	},
# 	{
# 		'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
# 	},
# ]

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/s/'

STATICFILES_DIRS = ( os.path.join(BASE_DIR, 'static'), )

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'collectstatic')

MEDIA_URL = '/m/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.contrib.auth.context_processors.auth',
				'django.template.context_processors.debug',
				'django.template.context_processors.i18n',
				'django.template.context_processors.media',
				'django.template.context_processors.static',
				'django.template.context_processors.tz',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

AUTH_USER_MODEL = 'user.User'

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/panel/'

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
