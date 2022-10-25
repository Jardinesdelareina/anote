from rest_framework import serializers
from .models import CustomUser


""" class RegistrationSerializer(serializers.ModelSerializer):
    # Создание нового пользователя
    # Требуется email, username и пароль, возвращается token

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'token')

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    # Аутентификация пользователя
    # Требуется email и пароль, возвращается token

    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    username = serializers.CharField(max_length=255, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        # Проверка данных пользователя

        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError('Для входа требуется email.')
        if password is None:
            raise serializers.ValidationError('Для входа требуется пароль')

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError('Пользователь с таким email и паролем не найден.')
        if not user.is_active:
            raise serializers.ValidationError('Такого пользователя не существует.')

        return {
            'token': user.token,
        }
 """

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
            'gender',
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
            'gender',
            'about',
            'birthday',
            'last_login',
            'date_joined',
        )
