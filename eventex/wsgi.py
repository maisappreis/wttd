"""
WSGI config for eventex project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eventex.settings')

application = Cling(get_wsgi_application())

# O Cling é uma aplicação wsgi
# A requisição do servidor web vai passar primeiro para o Cling
# Que quando acaba seu trabalho, delega para a função que está dentro dele.