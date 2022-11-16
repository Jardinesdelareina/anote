from django.core.exceptions import ValidationError

def get_path_upload_avatar(instance, file):
    # Построение пути к файлу аватара
    return f'user_{instance.id}/avatar/{file}'

def get_path_upload_article_image(instance, file):
    # Построение пути к файлу аватара
    return f'user_{instance.id}/articles/{file}'

def validate_size_image(file_obj):
    # Валидация размера загружаемого аватара
    size_limit = 2
    if file_obj.size > size_limit * 1024 * 1024:
        return ValidationError(f'Максимальный размер загружаемого файла {size_limit}Mb')
