from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, parsers
from ..utils.tools import delete_old_file
from .serializers import CustomUserSerializer, CustomUserPublicSerializer
from .models import CustomUser


class CustomUserView(ModelViewSet):
    # Вывод профиля пользователя
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)

    def perform_destroy(self, instance):
        # Удаление старого avatar во время загрузки нового
        delete_old_file(instance.avatar.path)
        instance.delete()


class CustomUserPublicView(ModelViewSet):
    # Вывод публичного профиля пользователя
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserPublicSerializer
    permission_classes = [permissions.AllowAny]
