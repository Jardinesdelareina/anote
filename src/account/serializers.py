from rest_framework import serializers
from .models import AnoteUser


class AnoteUserSerializer(serializers.ModelSerializer):
    # Информация о пользователе
    avatar = serializers.ImageField(read_only=True)
    class Meta:
        model = AnoteUser
        fields = (
            'id',
            'display_name',
            'avatar',
            'email',
            'phone',
            'gender',
            'birthday',
            'last_login',
            'is_active',
            'date_joined',
        )


class AnoteUserPublicSerializer(serializers.ModelSerializer):
    # Публичная информация о пользователе
    class Meta:
        model = AnoteUser
        fields = (
            'id',
            'display_name',
            'avatar',
            'gender',
            'last_login',
            'date_joined',
        )
