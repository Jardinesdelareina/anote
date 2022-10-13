from django.urls import path
from .views import (
    CommentViewSet,
    ArticleViewSet, 
    ArticleListViewSet,
    CategoryViewSet
) 

urlpatterns = [
    path('category', CategoryViewSet.as_view({'get': 'list'})),
    path('article/<int:pk>', ArticleViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('article', ArticleListViewSet.as_view({'get': 'list'})),
    path('comment/<int:pk>', CommentViewSet.as_view({'post': 'create'})),
    path('comment', CommentViewSet.as_view({'put': 'update', 'delete': 'deatroy'}))
]
