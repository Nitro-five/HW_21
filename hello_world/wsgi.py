import os
import sys

# Укажи путь к каталогу, где находятся твои файлы проекта
path = '/home/Maksym/mysite'  # Путь к папке с проектом (проверь, что путь правильный)
if path not in sys.path:
    sys.path.append(path)

# Указываем настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_world.settings')

# Импортируем WSGI приложение Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
