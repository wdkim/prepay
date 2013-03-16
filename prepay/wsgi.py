import os
import sys
import django.core.handlers.wsgi

path = '/Users/mike/emory/cs370/prepay'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'prepay.settings'

application = django.core.handlers.wsgi.WSGIHandler()
