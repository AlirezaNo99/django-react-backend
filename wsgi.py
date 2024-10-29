import sys
import os
from pathlib import Path

# Set the project base directory
base_dir = Path(__file__).resolve().parent

# Add the project base directory to the sys.path
sys.path.insert(0, str(base_dir))

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'

# Import the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
