"""
Django settings for kalenwallin project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import socket
from pathlib import Path

import environ

socket.getaddrinfo("localhost", 8080)

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True if env("DEBUG") == "True" else False

ALLOWED_HOSTS = [
    ".vercel-app",
    ".now.sh",
    "v2.kalenwallin.com",
    "localhost",
    ".kalenwallin.com",
    "kalenwallin.com",
    "dj.kalenwallin.com",
    ".vercel.app",
]

# Markdownfield requirement
SITE_URL = "v2.kalenwallin.com"

# Application definition

INSTALLED_APPS = [
    "portfolio.apps.PortfolioConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "autoslug",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

ROOT_URLCONF = "kalenwallin.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "kalenwallin.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": env("DATABASE_HOST"),
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASSWORD"),
        "PORT": env("DATABASE_PORT"),
    }
    # 'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
    # }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": """django.contrib.auth.password_validation
        .UserAttributeSimilarityValidator""",
    },
    {
        "NAME": """django.contrib.auth.password_validation
        .MinimumLengthValidator""",
    },
    {
        "NAME": """django.contrib.auth.password_validation
        .CommonPasswordValidator""",
    },
    {
        "NAME": """django.contrib.auth.password_validation
        .NumericPasswordValidator""",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Backblaze B2 Buckets based on AWS S3
# AWS_ACCESS_KEY_ID = env("BACKBLAZE_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = env("BACKBLAZE_SECRET_ACCESS_KEY")
# AWS_S3_REGION_NAME = env("BACKBLAZE_REGION")
# AWS_S3_ENDPOINT_URL = env("BACKBLAZE_URL")

# # files settings
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

BACKBLAZE_URL = env("BACKBLAZE_URL")
MEDIA_ROOT = BASE_DIR / "mediafiles"
MEDIA_URL = BACKBLAZE_URL + "/media/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_build", "static")

CORS_ORIGIN_WHITELIST = ["http://localhost:8080", "https://v2.kalenwallin.com"]
