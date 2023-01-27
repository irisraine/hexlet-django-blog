from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=200)  # название статьи
    body = models.TextField()  # тело статьи
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.CharField(max_length=64, blank=True)  # имя автора
    body = models.TextField()  # тело комментария
    timestamp = models.DateTimeField(auto_now_add=True)
    commented_article = models.ForeignKey(Article, on_delete=models.CASCADE)
