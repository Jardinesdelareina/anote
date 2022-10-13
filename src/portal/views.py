from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .permissions import IsAuthor
from .serializers import (
    CommentCreateSerializer, 
    CategoryArticleSerializer, 
    ArticleSerializer, 
    ArticleListSerializer
)
from .models import Category, Article, Comment


class CommentViewSet(ModelViewSet):
    # Вывод комментария к статье
    serializer_class = CommentCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes_by_action = {
        'update': [IsAuthor],
        'destroy': [IsAuthor],
    }
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()


class ArticleViewSet(ModelViewSet):
    # Вывод статьи
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes_by_action = {
        'get': [permissions.AllowAny],
        'update': [IsAuthor],
        'destroy': [IsAuthor],
    }
    queryset = Article.objects.all().select_related('categories').prefetch_related('comments')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ArticleListViewSet(ModelViewSet):
    # Вывод списка статей
    serializer_class = ArticleListSerializer
    queryset = Article.objects.all().select_related('category')


class CategoryViewSet(ModelViewSet):
    # Вывод категории статей
    serializer_class = CategoryArticleSerializer
    queryset = Category.objects.all()
