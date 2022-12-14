"""
WSGI config for django_k8s project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import pathlib

import dotenv

from django.core.wsgi import get_wsgi_application

CURRENT_DIR = pathlib.Path(__file__).resolve().parent #TODO: burayi incele
BASE_DIR = CURRENT_DIR.parent #TODO: burayi incele 
ENV_FILE_PATH = BASE_DIR / ".env" #TODO burayi incele 

dotenv.read_dotenv(str(ENV_FILE_PATH)) #TODO: bunu da anla

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_k8s.settings')

application = get_wsgi_application()
