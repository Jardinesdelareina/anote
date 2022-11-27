from django.urls import path
from .views import (
    CommentViewSet,
    ArticleViewSet, 
    ArticleListViewSet,
    SearchArticleList,
    CategoryViewSet,
    CategoryArticlesViewSet
) 

urlpatterns = [
    path('category/all', CategoryViewSet.as_view({'get': 'list'})),
    path('category/<int:category_id>', CategoryArticlesViewSet.as_view({'get': 'list'})),

    path('article/<int:pk>', ArticleViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('article/create', ArticleViewSet.as_view({'post': 'create'})),
    path('article/all', ArticleListViewSet.as_view({'get': 'list'})),
    path('search', SearchArticleList.as_view()),

    path('comment/create', CommentViewSet.as_view({'post': 'create'})),
    path('comment/<int:pk>', CommentViewSet.as_view({'put': 'update', 'delete': 'destroy'}))
]
