from django.urls import path
from .views import (
    CommentView,
    ArticleView, 
    ArticleListView,
    SearchArticleList,
    CategoryView,
    CategoryArticlesView,
) 

urlpatterns = [
    path('category/all', CategoryView.as_view({'get': 'list'})),
    path('category/<int:category_id>', CategoryArticlesView.as_view({'get': 'list'})),

    path('article/<int:pk>', ArticleView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('article/create', ArticleView.as_view({'post': 'create'})),
    path('article/all', ArticleListView.as_view({'get': 'list'})),
    path('search', SearchArticleList.as_view()),

    path('comment/create', CommentView.as_view({'post': 'create'})),
    path('comment/<int:pk>', CommentView.as_view({'put': 'update', 'delete': 'destroy'}))
]
