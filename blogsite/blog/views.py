
from django.shortcuts import render


def home_page(request):
    return render(request, 'index.html', {'title': 'Главная'})


def about_page(request):
    return render(request, 'about.html', {'title': 'О блоге'})


def post_page(request):
    return render(request, 'post.html', {'title': 'Страница поста'})
