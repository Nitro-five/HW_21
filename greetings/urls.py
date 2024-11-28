from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
"""
Маршруты для блога:
- Главная страница сайта ('home') отображает главную страницу блога.
- Страница подробностей поста ('post_detail') показывает информацию о посте по его идентификатору (post_id).
- Страница регистрации нового пользователя ('register') обрабатывает процесс регистрации.
- Страница входа пользователя ('login') обрабатывает процесс авторизации.
- Страница выхода пользователя ('logout') обрабатывает процесс выхода.
"""
