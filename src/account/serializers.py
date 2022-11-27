from rest_framework import serializers
from ..utils.tools import delete_old_file
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    # Информация о пользователе
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'avatar',
            'email',
            'about',
        )

    def update(self, instance, validated_data):
        delete_old_file(instance.avatar.path)
        return super().update(instance, validated_data)


class CustomUserPublicSerializer(serializers.ModelSerializer):
    # Публичная информация о пользователе
    avatar = serializers.ImageField(read_only=True)
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'avatar',
            'about',
        )
