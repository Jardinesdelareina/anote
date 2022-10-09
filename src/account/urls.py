from django.urls import path
from .views import *

urlpatterns = [
    path('profile/<int:pk>', AccountDetailView.as_view(), name='profile'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
