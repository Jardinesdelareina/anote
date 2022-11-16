from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, filters
from rest_framework.generics import ListAPIView
from ..utils.permissions import IsOwner
from .serializers import (
    CommentCreateSerializer, 
    CategorySerializer, 
    ArticleSerializer,
    ArticleListSerializer
)
from .models import Category, Article, Comment


class CommentViewSet(ModelViewSet):
    # Вывод комментария к статье
    serializer_class = CommentCreateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes_by_action = {
        'update': [IsOwner],
        'destroy': [IsOwner],
    }
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        # При удалении комментария делает text: null и is_deleted: True
        instance.is_deleted = True
        instance.save()


class ArticleViewSet(ModelViewSet):
    # Вывод статьи
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes_by_action = {
        'get': [permissions.AllowAny],
        'update': [IsOwner],
        'destroy': [IsOwner],
    }
    queryset = Article.objects\
        .all()\
        .select_related('category')\
        .prefetch_related('comments')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ArticleListViewSet(ModelViewSet):
    # Вывод списка статей
    serializer_class = ArticleSerializer
    queryset = Article.objects\
        .all()\
        .select_related('category')


class CategoryViewSet(ModelViewSet):
    # Вывод списка категорий статей
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryArticlesViewSet(ModelViewSet):
    # Вывод статей определенной категории
    serializer_class = ArticleListSerializer
    
    def get_queryset(self):
        return Article.objects\
            .filter(category_id=self.kwargs['category_id'], is_published=True)\
            .select_related('category') 


class SearchArticleList(ListAPIView):
    # Вывод результатов поиска
    queryset = Article.objects.filter(is_published=True)
    serializer_class = ArticleListSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title',]
