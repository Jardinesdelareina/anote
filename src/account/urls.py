from django.urls import path
from .views import CustomUserView, CustomUserPublicView

urlpatterns = [
    path('pu/<int:pk>', CustomUserPublicView.as_view({'get': 'retrieve'})),
    path('u/<int:pk>', CustomUserView.as_view({'get': 'retrieve', 'put': 'update'})),
]
