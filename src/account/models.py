from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from ..utils.tools import get_path_upload_avatar, validate_size_image
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    # Кастомная модель пользователя
    username = models.CharField('Имя', max_length=50, unique=True)
    email = models.EmailField('Email', unique=True)
    avatar = models.ImageField(
        'Аватар', 
        upload_to=get_path_upload_avatar,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_image],
        default=settings.DEFAULT_AVATAR,
        blank=True, 
        null=True,
    )
    about = models.TextField('О себе', max_length=1000, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-date_joined']
