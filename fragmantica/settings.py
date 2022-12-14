"""
Django settings for fragmantica project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

import cloudinary
from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

# ALLOWED_HOSTS =['localhost','127.0.0.1',]
ALLOWED_HOSTS =[]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'cloudinary',

    'fragmantica.accounts',
    'fragmantica.common',
    'fragmantica.perfumes',
    'fragmantica.designers',
    'fragmantica.notes',
    'fragmantica.awards',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fragmantica.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
		,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fragmantica.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

#TODO/ADD Postgres
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fragmantica_db_pg',
        'USER': 'postgres-user',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

#TODO
if DEBUG:
    AUTH_PASSWORD_VALIDATORS=[]
else:

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS=(BASE_DIR / 'staticfiles',)


MEDIA_URL='media/'
MEDIA_ROOT=BASE_DIR/'mediafiles'


cloudinary.config(
    cloud_name="da3gohuzx",
    api_key="815811933576927",
    api_secret="Gvzv7FQ6EZaXlTgjw0rXPFW-j0M",
    secure=True
)

# EMAIL_BACKEND = 'django_mailjet.backends.MailjetBackend'
# # MAILJET_API_KEY = 'API-KEY'
# # MAILJET_API_SECRET = 'API-SECRET'

#
# EMAIL_HOST='smtp.gmail.com'
# EMAIL_PORT=587
# EMAIL_USE_TLS=True
# EMAIL_HOST_USER='fragmantica.django@gmail.com'
# EMAIL_HOST_PASSWORD = 'imasucgushyqcein'

EMAIL_HOST='in-v3.mailjet.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='fragmantica.django@gmail.com'
EMAIL_HOST_PASSWORD = '$YdfSBkR9LXpjtD7'


EMAIL_BACKEND = 'django_mailjet.backends.MailjetBackend'
# MAILJET_API_KEY = 'API-KEY'
# MAILJET_API_SECRET = 'API-SECRET'

MAILJET_API_KEY= config("MAILJET_API_KEY")
MAILJET_API_SECRET = config("MAILJET_API_SECRET")


# DEFAULT_FROM_EMAIL='fragmantica.django@gmail.com'
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL='accounts.FragUser'

LOGIN_REDIRECT_URL=reverse_lazy('index')