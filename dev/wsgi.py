"""
WSGI config for analytics project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#TODO test running this with gunicorn
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dev.settings.production")

application = get_wsgi_application()
