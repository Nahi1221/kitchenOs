"""
Production settings patch for PythonAnywhere.
This file is loaded AFTER settings.py on PythonAnywhere by setting
DJANGO_SETTINGS_MODULE = "kitchenos.settings_prod".

Usage on PythonAnywhere:
  1. Upload this file to ~/kitchenos/kitchenos/settings_prod.py
  2. In the PythonAnywhere Web tab, set the WSGI file to:
        import sys, os
        sys.path.insert(0, os.path.expanduser('~/kitchenos'))
        os.environ['DJANGO_SETTINGS_MODULE'] = 'kitchenos.settings_prod'
        from kitchenos.wsgi import application
     (OR just point DJANGO_SETTINGS_MODULE to settings_prod in wsgi.py)
  3. Set environment variables in the PythonAnywhere Web tab
     (ALLOWED_HOST, SECRET_KEY, DEBUG=False, etc.)
"""

from .settings import *  # noqa: F401,F403

import os

DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    h.strip() for h in os.environ.get(
        "ALLOWED_HOST",
        "yourusername.pythonanywhere.com"
    ).split(",") if h.strip()
]

CORS_ALLOWED_ORIGINS = [
    f"https://{ALLOWED_HOSTS[0]}" if ALLOWED_HOSTS else "",
    "https://yourusername.pythonanywhere.com",
]
CORS_ALLOWED_ORIGIN_REGEXES = [r"^https://.*\.pythonanywhere\.com$"]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")  # noqa: F405
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True