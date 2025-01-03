"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR is the root directory of the Django project
BASE_DIR = Path(__file__).resolve().parent.parent

# TEMPLATES_DIR defines the path to the templates directory
TEMPLATES_DIR = BASE_DIR / "project/templates"

SECRET_KEY = 'django-insecure-o4gkync!zq49gc)bv@!1hlb0i_@!1p_9pyd+m94i-@y!-8b+93'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG determines if the project is in debug mode. Should be False in production
DEBUG = True
#
# CSRF_COOKIE_SECURE = False
# CSRF_COOKIE_HTTPONLY = False

# ALLOWED_HOSTS defines the allowed hostnames for the Django application
ALLOWED_HOSTS = ["*"]

# LOGIN_URL is the url to redirect when the user is not logged in
LOGIN_URL = '/signin/'

CSRF_TRUSTED_ORIGINS = [
    'https://skillhub.koyeb.app',
]

# Application definition
# INSTALLED_APPS lists all the applications that django will use
INSTALLED_APPS = [
    'django.contrib.admin',  # Django admin application
    'django.contrib.auth',  # Django authentication application
    'django.contrib.contenttypes',  # Django contenttypes application
    'django.contrib.sessions',  # Django sessions application
    'django.contrib.messages',  # Django message framework
    'spApp',  # Your custom app
    'django.contrib.staticfiles',  # Django static files application
]

# MIDDLEWARE defines the components that will modify requests and responses
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise middleware for serving static files
    'django.contrib.sessions.middleware.SessionMiddleware',  # Sessions middleware
    'django.middleware.common.CommonMiddleware',  # Common middleware
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF middleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Authentication middleware
    'django.contrib.messages.middleware.MessageMiddleware',  # Message middleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking protection middleware
]

# ROOT_URLCONF defines where django should look for the root urls
ROOT_URLCONF = 'project.urls'

# TEMPLATES define the configuration of the template engine
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Template engine
        'DIRS': [TEMPLATES_DIR],  # Directory where Django should search for templates
        'APP_DIRS': True,  # If templates should be found within the apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # debug processor
                'django.template.context_processors.request',  # Request processor
                'django.contrib.auth.context_processors.auth',  # Authentication processor
                'django.contrib.messages.context_processors.messages',  # Message processor
            ],
        },
    },
]

# WSGI_APPLICATION defines the WSGI application that django will use
WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# DATABASES defines database configurations for django project
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Database engine
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # Database name
    }
}

# Media files configuration
# MEDIA_URL is the URL to be used to access media files
MEDIA_URL = '/media/'

# MEDIA_ROOT is the absolute path in the server to where uploaded media files are saved
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
# AUTH_PASSWORD_VALIDATORS lists password validators
AUTH_PASSWORD_VALIDATORS = []

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/
# LANGUAGE_CODE defines the language of django
LANGUAGE_CODE = 'en-us'

# TIME_ZONE defines the time zone django should use
TIME_ZONE = 'UTC'

# USE_I18N determines if django should be used for translations
USE_I18N = True

# USE_TZ determines if django should use time zones
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
# STATIC_URL is the url to access static files
STATIC_URL = '/static/'

# The directory where static files will be stored
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'project/static'),  # Adjust this path according to your project structure
]

# Default primary key field typeش
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
# DEFAULT_AUTO_FIELD defines the type of the default primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
