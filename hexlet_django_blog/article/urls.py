from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='articles'),
    path('<int:id>/', views.ArticleView.as_view(), name='article'),
    path('<int:id>/comment/', views.CommentArticleView.as_view(), name='comment_create'),
    path('create/', views.ArticleFormCreateView.as_view(), name='articles_create'),
    path('<int:id>/edit/', views.ArticleFormEditView.as_view(), name='articles_update'),
    path('<int:id>/delete/', views.ArticleFormDeleteView.as_view(), name='articles_delete'),
]
