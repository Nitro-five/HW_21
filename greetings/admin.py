from django.contrib import admin
from .models import Post, Category, Comment

# Регистрирует модель Post в административном интерфейсе Django
admin.site.register(Post)

# Регистрирует модель Category в административном интерфейсе Django
admin.site.register(Category)

# Регистрирует модель Comment в административном интерфейсе Django
admin.site.register(Comment)
