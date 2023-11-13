from django.urls import path
from hexlet_django_blog.article import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='articles'),
    path('<tags>/<int:article_id>/', views.index, name='article')
]
