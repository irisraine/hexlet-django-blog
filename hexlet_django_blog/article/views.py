from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator
from hexlet_django_blog.article.models import Article
from .forms import CommentArticleForm, ArticleForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        page = int(request.GET.get('page', '1'))
        if query:
            articles = Article.objects.filter(Q(name__icontains=query))
        else:
            articles = Article.objects.all().order_by('id')
        articles_paginator = Paginator(articles, 8)
        return render(request, 'articles/index.html', context={
            'articles': articles_paginator.get_page(page),
            'query': query,
            'num_pages': articles_paginator.num_pages
        })


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article
        })


class CommentArticleView(View):
    def get(self, request, *args, **kwargs):
        form = CommentArticleForm()
        return render(request, 'comment.html', context={
            'form': form,
            'id': kwargs['id']
        })


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
        return render(request, 'articles/create.html', {'form': form})


class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {'form': form, 'article_id': article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')
        return render(request, 'articles/update.html', {'form': form, 'article_id': article_id})


class ArticleFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect('articles')