"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
from os.path import join,dirname,abspath
PROJECT_DIR = dirname(dirname(abspath(__file__)))

import sys
sys.path.append("/var/www/portfolio")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
