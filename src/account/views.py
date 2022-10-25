from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import CustomUserSerializer, CustomUserPublicSerializer
from .models import CustomUser


class CustomUserViewSet(ModelViewSet):
    # Вывод профиля пользователя
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)


class CustomUserPublicViewSet(ModelViewSet):
    # Вывод публичного профиля пользователя
    serializer_class = CustomUserPublicSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        return CustomUser.objects.all()
