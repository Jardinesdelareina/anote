from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class AnoteUserManager(BaseUserManager):
    # Диспетчер кастомной модели пользователя с уникальным идентификатором email

    def create_user(self, email, password, **extra_fields):
        # Создание и сохранение пользователя
        if not email:
            raise ValueError(_('У пользователя должна быть электронная почта'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        # Создание и сохранение администратора
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Администратор должен иметь is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Администратор должен иметь is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
