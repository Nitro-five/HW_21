# To use your own django app use code like this:
import os
import sys

#
## assuming your django settings file is at '/home/Maksym/mysite/mysite/settings.py'
## and your manage.py is is at '/home/Maksym/mysite/manage.py'
path = '/home/Maksym/HW_21'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'HW_21.hello_world.settings'
#
# then:
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
