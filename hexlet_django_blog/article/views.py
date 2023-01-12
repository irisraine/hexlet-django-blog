from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'article/index.html', context={
        'article_name': 'hexlet_django_blog',
    })

