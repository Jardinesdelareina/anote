from django.urls import path
from .views import CustomUserViewSet, CustomUserPublicViewSet

urlpatterns = [
    path('<int:pk>', CustomUserPublicViewSet.as_view({'get': 'retrieve'})),
    path('account/<int:pk>', CustomUserViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
]
