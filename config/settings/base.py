"""
Project setting configuration
Note: DRF-Project config
"""

from pathlib import Path
import environ
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ROOT_DIR = (
        environ.Path(__file__) - 3
)

ENV = environ.Env()
ENV.read_env(f"{ROOT_DIR}/.env")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENV.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENV.bool('DJANGO_DEBUG', False)
ALLOWED_HOSTS = ENV.list('ALLOWED_HOSTS')

# Application definition
from config.settings.app import INSTALLED_APPS

# Importing middleware

from config.settings.middleware import MIDDLEWARE

ROOT_URLCONF = 'config.urls'

"""
Importing template configuration
currently required to serve admin dashboard
"""

from config.settings.admin import TEMPLATES

WSGI_APPLICATION = 'config.wsgi.application'

# DRF config

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

"""
Reference doc: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
"""
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

AUTH_USER_MODEL = 'service.User'

# Importing database configuration

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': ENV.str('DB_NAME'),
        'USER': ENV.str('USER'),
        'PASSWORD': ENV.str('PASSWORD'),
        'HOST': ENV.str('HOST'),
        'PORT': ENV.int('PORT'),
        # 'ATOMIC_REQUESTS': True,
        'TEST': {
            'NAME': ENV.str('TEST_DB_NAME'),
        }
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
