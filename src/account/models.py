from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.conf import settings
from .utils import get_path_upload_avatar, validate_size_avatar
from .managers import CustomUserManager
import datetime
import jwt


class CustomUser(AbstractUser):
    # Кастомная модель пользователя

    GENDER = {
        ('male', 'Мужской'),
        ('female', 'Женский')
    }

    username = models.CharField('Имя', max_length=50, unique=True)
    email = models.EmailField('Email', unique=True)
    phone = models.CharField('Телефон', max_length=14, unique=True, blank=True, null=True)
    avatar = models.ImageField(
        'Аватар', 
        upload_to=get_path_upload_avatar,
        blank=True, 
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_avatar]
    )
    gender = models.CharField('Пол', max_length=7, choices=GENDER, default='male')
    about = models.TextField('О себе', max_length=1000, blank=True, null=True)
    birthday = models.DateField('Дата рождения', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    """ @property
    def token(self):
        # Вызов токена пользователя через user.token вместо user._generate_jwt_token
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def _generate_jwt_token(self):
        # Создание JWT пользователя, срок действия 60 дней
        dt = datetime.datetime.now() + datetime.timedelta(days=60)
        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')
 """
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-date_joined']
