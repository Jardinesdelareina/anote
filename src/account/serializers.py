from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    # Информация о пользователе
    avatar = serializers.ImageField(read_only=True)
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'avatar',
            'email',
            'phone',
            'about',
            'birthday',
            'last_login',
            'date_joined',
        )


class CustomUserPublicSerializer(serializers.ModelSerializer):
    # Публичная информация о пользователе
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'avatar',
            'about',
            'last_login',
            'date_joined',
        )
