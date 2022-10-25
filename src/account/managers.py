from django.contrib.auth.base_user import BaseUserManager


class AnoteUserManager(BaseUserManager):
    # Диспетчер кастомной модели пользователя

    def create_user(self, email, username, password, **extra_fields):
        # Создание и сохранение пользователя
        if not email:
            raise ValueError('У пользователя должна быть электронная почта')
        if not username:
            raise ValueError('У пользователя должно быть имя')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        # Создание и сохранение администратора
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Администратор должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Администратор должен иметь is_superuser=True.')
        return self.create_user(email, username, password, **extra_fields)
