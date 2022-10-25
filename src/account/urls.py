from django.urls import path
from .views import AnoteUserViewSet, AnoteUserPublicViewSet

urlpatterns = [
    path('<int:pk>', AnoteUserPublicViewSet.as_view({'get': 'retrieve'})),
    path('account/<int:pk>', AnoteUserViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
]
