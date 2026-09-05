import os
from pathlib import Path

from dotenv import load_dotenv
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================
#
# Local development:
#     Uses .env
#
# Vercel:
#     Uses Vercel Environment Variables
#
# =========================================================

load_dotenv(BASE_DIR / ".env")


# =========================================================
# BASIC SETTINGS
# =========================================================

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "dev-secret-change-this",
)

DEBUG = os.getenv(
    "DEBUG",
    "True",
).lower() == "true"


# =========================================================
# ALLOWED HOSTS
# =========================================================

default_allowed_hosts = (
    "127.0.0.1,"
    "localhost,"
    ".vercel.app"
)

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv(
        "ALLOWED_HOSTS",
        default_allowed_hosts,
    ).split(",")
    if host.strip()
]


# =========================================================
# INSTALLED APPS
# =========================================================

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Cloudinary
    "cloudinary_storage",
    "cloudinary",

    # Portfolio apps
    "core",
    "portfolio",
    "projects",
    "contact",
    "blog",
]


# =========================================================
# MIDDLEWARE
# =========================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =========================================================
# URL / TEMPLATES
# =========================================================

ROOT_URLCONF = "config.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates",
        ],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core.context_processors.site_context",
            ],
        },
    },
]


# =========================================================
# WSGI / ASGI
# =========================================================

WSGI_APPLICATION = "config.wsgi.application"

ASGI_APPLICATION = "config.asgi.application"


# =========================================================
# DATABASE
# =========================================================
#
# Local:
#     SQLite
#
# Production:
#     Neon PostgreSQL through DATABASE_URL
#
# =========================================================

DATABASE_URL = os.getenv("DATABASE_URL")


if DATABASE_URL:

    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            ssl_require=True,
        )
    }

else:

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# =========================================================
# PASSWORD VALIDATION
# =========================================================

AUTH_PASSWORD_VALIDATORS = []


# =========================================================
# INTERNATIONALIZATION
# =========================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Dhaka"

USE_I18N = True

USE_TZ = True


# =========================================================
# STATIC FILES
# =========================================================

STATIC_URL = "/static/"


STATICFILES_DIRS = [
    BASE_DIR / "static",
]


STATIC_ROOT = BASE_DIR / "staticfiles"


# =========================================================
# CLOUDINARY MEDIA STORAGE
# =========================================================
#
# Images and other uploaded media are stored in Cloudinary
# instead of the local/Vercel filesystem.
#
# Credentials come from environment variables.
#
# =========================================================

MEDIA_URL = "/media/"


CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv(
        "CLOUDINARY_CLOUD_NAME"
    ),

    "API_KEY": os.getenv(
        "CLOUDINARY_API_KEY"
    ),

    "API_SECRET": os.getenv(
        "CLOUDINARY_API_SECRET"
    ),
}


# =========================================================
# DJANGO STORAGE BACKENDS
# =========================================================
#
# default:
#     Cloudinary for uploaded media
#
# staticfiles:
#     WhiteNoise for static files
#
# =========================================================

STORAGES = {
    "default": {
        "BACKEND": (
            "cloudinary_storage.storage."
            "MediaCloudinaryStorage"
        ),
    },

    "staticfiles": {
        "BACKEND": (
            "whitenoise.storage."
            "CompressedManifestStaticFilesStorage"
        ),
    },
}


# =========================================================
# DJANGO DEFAULTS
# =========================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# =========================================================
# LOGIN
# =========================================================

LOGIN_URL = "/admin/login/"


# =========================================================
# SECURITY
# =========================================================

SECURE_REFERRER_POLICY = os.getenv(
    "SECURE_REFERRER_POLICY",
    "strict-origin-when-cross-origin",
)


SECURE_CONTENT_TYPE_NOSNIFF = True


X_FRAME_OPTIONS = "DENY"


# =========================================================
# PRODUCTION HTTPS SECURITY
# =========================================================

if not DEBUG:

    SECURE_SSL_REDIRECT = True

    SESSION_COOKIE_SECURE = True

    CSRF_COOKIE_SECURE = True

    SECURE_PROXY_SSL_HEADER = (
        "HTTP_X_FORWARDED_PROTO",
        "https",
    )


# =========================================================
# CSRF TRUSTED ORIGINS
# =========================================================

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "CSRF_TRUSTED_ORIGINS",
        "https://*.vercel.app",
    ).split(",")
    if origin.strip()
]