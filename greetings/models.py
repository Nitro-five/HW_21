from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Category(models.Model):
    """
    Модель для категории поста.
    Каждый объект категории имеет название (name).
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Возвращает строковое представление категории.
        """
        return self.name


class Post(models.Model):
    """
    Модель для поста блога.
    Каждый пост имеет заголовок (title), содержание (content),
    дату создания (created_at), категорию (category) и теги (tags).
    """
    objects = None
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = TaggableManager()

    def __str__(self):
        """
        Возвращает строковое представление поста (его заголовок).
        """
        return self.title


class Comment(models.Model):
    """
    Модель для комментариев к посту.
    Каждый комментарий связан с постом (post), имеет автора (author),
    содержание (content) и дату создания (created_at).
    """
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Возвращает строковое представление комментария.
        """
        return f'Comment by {self.author}'


class Profile(models.Model):
    """
    Модель для профиля пользователя.
    Связан с объектом пользователя (user) и может содержать биографию (bio).
    """
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        """
        Возвращает строковое представление профиля пользователя (его имя пользователя).
        """
        return self.user.username
