from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import AnoteUserSerializer, AnoteUserPublicSerializer
from .models import AnoteUser


class AnoteUserViewSet(ModelViewSet):
    # Вывод профиля пользователя
    serializer_class = AnoteUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AnoteUser.objects.filter(id=self.request.user.id)


class AnoteUserPublicViewSet(ModelViewSet):
    # Вывод публичного профиля пользователя
    serializer_class = AnoteUserPublicSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        return AnoteUser.objects.all()
