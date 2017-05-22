# Python
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings')

# Django
from django.core.wsgi import get_wsgi_application  # noqa

# Whitenoise
from whitenoise.django import DjangoWhiteNoise  # noqa


application = get_wsgi_application()
application = DjangoWhiteNoise(application)
