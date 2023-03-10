from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator
from hexlet_django_blog.article.models import Article, Comment
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
        comments = article.comment_set.all()
        return render(request, 'articles/show.html', context={
            'article': article,
            'comments': comments
        })


class CommentArticleView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs['id']
        form = CommentArticleForm()
        article = Article.objects.get(id=article_id)
        return render(request, 'comment.html', context={
            'form': form,
            'id': kwargs['id'],
            'article_name': article.name
        })

    def post(self, request, *args, **kwargs):
        article_id = kwargs['id']
        form = CommentArticleForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if not comment.author:
                comment.author = "Анон"
            comment.commented_article = Article.objects.get(id=article_id)
            comment.save()
        return redirect('article', id=article_id)


class ArticleCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
        return render(request, 'articles/create.html', {'form': form})


class ArticleEditView(View):
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


class ArticleDeleteView(View):
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect('articles')


class CommentArticleDeleteView(View):
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        comment_id = kwargs.get('comment_id')
        article = Article.objects.get(id=article_id)
        comment = Comment.objects.get(commented_article=article, id=comment_id)
        comment.delete()
        return redirect('article', id=article_id)
