from pathlib import Path

from django.conf.global_settings import LOGGING_CONFIG
from dotenv import load_dotenv
from os import getenv, path

from drf_spectacular.settings import SPECTACULAR_DEFAULTS
from loguru import logger
from datetime import timedelta


# Base directory
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

APPS_DIR = BASE_DIR / "core_apps"

local_env_file = path.join(BASE_DIR, ".envs", ".env.local")

if path.isfile(local_env_file):
    load_dotenv(local_env_file)



# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "django_filters",
    "django_countries",
    "phonenumber_field",
    "drf_spectacular",
    "djoser",
    "cloudinary",
    "django_celery_beat",
    "djcelery_email"
]

LOCAL_APPS = ["core_apps.user_auth", "core_apps.common", "core_apps.user_profile"]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(APPS_DIR / "templates")],
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

WSGI_APPLICATION = "config.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": getenv("POSTGRES_DB"),
        "USER": getenv("POSTGRES_USER"),
        "PASSWORD": getenv("POSTGRES_PASSWORD"),
        "HOST": getenv("POSTGRES_HOST"),
        "PORT": getenv("POSTGRES_PORT"),

    }
}

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]


# Password validation
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
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = str(BASE_DIR / "staticfiles")

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "user_auth.User"
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "BackEndProgrammer.com",
    "DESCRIPTION": "BackEndProgrammer.com",
    "VERSION": "0.0.1",
    "SERVE_INCLUDE_SCHEMA": False,
    "LICENSE": {
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
}

SITE_ID = 1

LOGGING_CONFIG = None

LOGURU_LOGGING = {
    "handlers": [
        {
            "sink":  BASE_DIR / "logs/debug.log",
            "level": "DEBUG",
            "filter": lambda record: record["level"].no <= logger.level('WARNING').no,
            "format": "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}: {function}:{line} - {message}",
            "rotation": "10MB",
            "retention": "30 days",
            "compression": "zip",

        },
        {

            "sink": BASE_DIR / "logs/error.log",
            "level": "ERROR",
            "format": "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}: {function}:{line} - {message}",
            "rotation": "10MB",
            "retention": "30 days",
            "compression": "zip",
            "backtrace": True,
            "diagnose": True,

        }

    ],
}

logger.configure(**LOGURU_LOGGING)

LOGGING = {

    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"loguru": {"class": "interceptor.InterceptHandler"}},
    "root": {"handlers": ["loguru"], "level": "DEBUG"},
}
