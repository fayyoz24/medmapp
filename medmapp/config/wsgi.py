"""
WSGI config for medmapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

from users.models import User
User.objects.create_superuser("admin", "admin@example.com", "12345678")
print("✅ Superuser created: admin / 12345678")