"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path
from typing import List

from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG: bool = config("DEBUG", cast=bool)


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "admins",
    "core",
    "contentsecurity",
    "csp",
]

MIDDLEWARE = [
    "csp.middleware.CSPMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "app.urls"

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

WSGI_APPLICATION = "app.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# @@@@@@@@@@@ Security Settings @@@@@@@@@@@

# 1. cookies

SESSION_COOKIE_SECURE = True  # HTTPS only session Cookies
CSRF_COOKIE_SECURE = True  # HTTPS only csrf cookies
SESSION_COOKIE_HTTPONLY = True  # Disallow js from accessing session cookies

# 2. HTTPS only
SECURE_SSL_REDIRECT = not DEBUG  # HTTPS only (in production)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # HTTPS for subdomains
SECURE_HSTS_SECONDS = 31536000  # Force browsers to refuse to connect insecurely (1y)
SECURE_HSTS_PRELOAD = True

# 3. Allowed hosts
ALLOWED_HOSTS: List[str] = config("ALLOWED_HOSTS").split()  # type:ignore

# 4. Admins
ADMINS = [("hamdy", "a@a.com")]

# 4. CORS

# add corsheaders to installed apps

# add 'corsheaders.middleware.CorsMiddleware', before 'corsheaders.middleware.CorsMiddleware'

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

AUTH_USER_MODEL = "core.user"

# CSP
CSP_IMG_SRC = ("'self'", "https://html.sammy-codes.com")
CSP_STYLE_SRC = (
    "'self'",
    "sha256-r5bInLZB0y6ZxHFpmz7cjyYrndjwCeDLDu/1KeMikHA=",
    "https://fonts.googleapis.com",
)
CSP_FONT_SRC = ("'self'", "https://fonts.gstatic.com/")
# Content Security Policy

CSP_INCLUDE_NONCE_IN = ["script-src"]
