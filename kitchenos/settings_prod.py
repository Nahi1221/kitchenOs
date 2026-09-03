"""Production settings overlay for managed hosting (Render, etc.)."""

from .settings import *  # noqa: F401,F403

import os

DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    h.strip() for h in os.environ.get(
        "ALLOWED_HOSTS",
        os.environ.get("ALLOWED_HOST", "localhost,127.0.0.1")
    ).split(",") if h.strip()
]

CORS_ALLOWED_ORIGINS = [
    o.strip() for o in os.environ.get("CORS_ALLOWED_ORIGINS", "").split(",") if o.strip()
]
if not CORS_ALLOWED_ORIGINS and os.environ.get("FRONTEND_URL"):
    CORS_ALLOWED_ORIGINS = [os.environ["FRONTEND_URL"]]

CSRF_TRUSTED_ORIGINS = [
    o.strip() for o in os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",") if o.strip()
]
if not CSRF_TRUSTED_ORIGINS and os.environ.get("FRONTEND_URL"):
    CSRF_TRUSTED_ORIGINS = [os.environ["FRONTEND_URL"]]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # noqa: F405
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True