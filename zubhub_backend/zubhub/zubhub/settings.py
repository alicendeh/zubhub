"""
Django settings for bookstore project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import socket
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENVIRONMENT = os.environ.get('ENVIRONMENT', default='production')

DEFAULT_DISPLAY_NAME = os.environ.get("DEFAULT_DISPLAY_NAME", default="ZubHub")
DEFAULT_FRONTEND_DOMAIN = os.environ.get(
    "DEFAULT_FRONTEND_DOMAIN", default="localhost:3000")
DEFAULT_BACKEND_DOMAIN = os.environ.get(
    "DEFAULT_BACKEND_DOMAIN", default="localhost:8000")
DEFAULT_FRONTEND_PROTOCOL = os.environ.get(
    "DEFAULT_FRONTEND_PROTOCOL", default="https")
DEFAULT_BACKEND_PROTOCOL = os.environ.get(
    "DEFAULT_BACKEND_PROTOCOL", default="https")
DEBUG = int(os.environ.get("DEBUG", default=0))
STORE_MEDIA_LOCALLY = bool(
    int(os.environ.get("STORE_MEDIA_LOCALLY", default=1)))
MEDIA_SECRET = os.environ.get("MEDIA_SECRET", default="")
DEFAULT_MEDIA_SERVER_PROTOCOL = os.environ.get(
    "DEFAULT_MEDIA_SERVER_PROTOCOL", default="http")
DEFAULT_MEDIA_SERVER_DOMAIN = os.environ.get(
    "DEFAULT_MEDIA_SERVER_DOMAIN", default="localhost:8001")

if DEFAULT_FRONTEND_DOMAIN.startswith("localhost"):
    FRONTEND_HOST = DEFAULT_FRONTEND_DOMAIN.split(":")[0]
else:
    FRONTEND_HOST = DEFAULT_FRONTEND_DOMAIN

if DEFAULT_BACKEND_DOMAIN.startswith("localhost"):
    BACKEND_HOST = DEFAULT_BACKEND_DOMAIN.split(":")[0]
else:
    BACKEND_HOST = DEFAULT_BACKEND_DOMAIN


if ENVIRONMENT == 'production':
    SECURE_BROWSER_XSS_FILTER = True
    # SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'SAMEORIGIN'

    # SESSION_COOKIE_SECURE = True
    # CSRF_COOKIE_SECURE = True

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['127.0.0.1', FRONTEND_HOST, "www." +
                 FRONTEND_HOST, BACKEND_HOST, "www."+BACKEND_HOST, "web"]
# ALLOWED_HOSTS = ['*']

# CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = (
    DEFAULT_FRONTEND_PROTOCOL+"://"+DEFAULT_FRONTEND_DOMAIN,
    DEFAULT_BACKEND_PROTOCOL+"://"+DEFAULT_BACKEND_DOMAIN,
    DEFAULT_FRONTEND_PROTOCOL+"://www."+DEFAULT_FRONTEND_DOMAIN,
    DEFAULT_BACKEND_PROTOCOL+"://www."+DEFAULT_BACKEND_DOMAIN,
    DEFAULT_MEDIA_SERVER_PROTOCOL+"://"+DEFAULT_MEDIA_SERVER_DOMAIN
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'djcelery_email',
    'django_celery_results',
    'crispy_forms',
    'debug_toolbar',
    'treebeard',
    'django_summernote',
    'zubhub',
    'APIS',
    'creators',
    'projects',
]

# askimet
AKISMET_API_KEY = os.environ.get("AKISMET_API_KEY")


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'post_anon': '20/min',
        'get_anon': '25/min',
        'post_user': '30/min',
        'get_user': '40/min',
        'sustained': '1500/day'
    }
}

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'creators.serializers.CustomRegisterSerializer',
}

ACCOUNT_ADAPTER = 'creators.adapter.CustomAccountAdapter'

AUTH_USER_MODEL = 'creators.Creator'


# django-allauth config
LOGIN_REDIRECT_URL = '/api'
ACCOUNT_LOGOUT_REDIRECT = '/api'

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
# ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True


CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'zubhub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'zubhub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POSTGRES_NAME"),
        'USER': os.environ.get("POSTGRES_USER"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
        'HOST': os.environ.get("POSTGRES_HOST"),
        'PORT': 5432
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'default_cache_table',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/api/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_FINDER = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
]

# django-debug-toolbar
if ENVIRONMENT != 'production':
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + '1' for ip in ips]

################################################################################
# How to setup Celery with Django
################################################################################

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BACKEND")


################################################################################
# How to send email in Django project with Celery
################################################################################

EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
CELERY_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'hello@unstructured.studio'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_API_KEY')
EMAIL_PORT = 465
EMAIL_USE_SSL = True


DEFAULT_FROM_PHONE = os.environ.get("DEFAULT_FROM_PHONE")
DEFAULT_WHATSAPP_FROM_PHONE = os.environ.get("DEFAULT_WHATSAPP_FROM_PHONE")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NOTIFY_SERVICE_SID = os.environ.get("TWILIO_NOTIFY_SERVICE_SID")

# EMAIL_PORT = 1025
CELERY_EMAIL_CHUNK_SIZE = 1
CELERY_EMAIL_TASK_CONFIG = {
    'name': 'djcelery_email_send',
    'ignore_result': False,
}


SUMMERNOTE_CONFIG = {

    # You can put custom Summernote settings
    'summernote': {
        # Change editor size
        'width': '100%',
        'max-width': '900',
        'height': '600',

        # Toolbar customization
        # https://summernote.org/deep-dive/#custom-toolbar-popover
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'clear']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['emoji', 'link', 'picture', 'video']]
        ]
    },
    "css": ("/static/css/summernote_plugin.css",),
    "js": ("/static/js/summernote_plugin.js",)
}
