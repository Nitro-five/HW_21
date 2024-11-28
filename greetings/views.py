from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import Post, Profile

def home(request):
    """
    Главная страница блога.
    Получает все посты и передает их в шаблон 'home.html' для отображения.
    """
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, post_id):
    """
    Страница с подробной информацией о посте и комментариями.
    При GET-запросе отображает пост и его комментарии.
    При POST-запросе добавляет новый комментарий и отправляет уведомление автору поста.
    """
    post = Post.objects.get(id=post_id)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            send_mail(
                'New Comment on Your Post',
                f'A new comment was posted on your post {post.title}.',
                'from@example.com',
                [post.author.email],
                fail_silently=False,
            )
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})

def register(request):
    """
    Страница регистрации нового пользователя.
    При GET-запросе отображает форму регистрации.
    При POST-запросе сохраняет нового пользователя и создаёт профиль.
    Также отправляется письмо с подтверждением регистрации.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            send_mail(
                'Welcome to our Blog!',
                'Thank you for registering on our blog.',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    """
    Страница входа пользователя.
    При GET-запросе отображает форму для входа.
    При POST-запросе проверяет данные формы и выполняет вход.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    """
    Страница выхода пользователя.
    Выходит из системы и перенаправляет на страницу входа.
    """
    logout(request)
    return redirect('login')
