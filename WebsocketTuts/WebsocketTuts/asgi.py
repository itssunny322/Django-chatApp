from email.mime import application
import os

import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebsocketTuts.settings')

django.setup()

application = get_default_application()