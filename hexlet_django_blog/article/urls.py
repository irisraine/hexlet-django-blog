from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='articles'),
    path('<int:id>/', views.ArticleView.as_view(), name='article'),
    path('<int:id>/comment/', views.CommentArticleView.as_view(), name='comment_create'),
    path('create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('<int:id>/edit/', views.ArticleEditView.as_view(), name='article_update'),
    path('<int:id>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:id>/comment/<int:comment_id>/delete/', views.CommentArticleDeleteView.as_view(), name='comment_delete'),
]
