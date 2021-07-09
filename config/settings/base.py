"""
Project setting configuration
Note: DRF-Project config
"""

from pathlib import Path
import environ

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
        'rest_framework.authentication.TokenAuthentication',
    ]
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
