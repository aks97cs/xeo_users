# Project App Configuration

INBUILT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
]

CUSTOM_APPS = [
    'service.apps.ServiceConfig',
]
INSTALLED_APPS = INBUILT_APPS + THIRD_PARTY_APPS + CUSTOM_APPS
