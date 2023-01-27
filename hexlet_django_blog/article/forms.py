from django import forms
from django.forms import ModelForm
from .models import Article, Comment


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']
        labels = {
            'name': 'Имя',
            'body': 'Текст статьи'
        }


class CommentArticleForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body']
        labels = {
            'author': 'Автор',
            'body': 'Текст комментария'
        }
