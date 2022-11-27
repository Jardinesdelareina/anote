from django.db import models
from django.urls import reverse
from django.conf import settings
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.core.validators import FileExtensionValidator
from ..utils.tools import get_path_upload_article_image, validate_size_image


class Category(models.Model):
    # Модель категории статьи
    title = models.CharField('Название', max_length=50)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Article(models.Model):
    # Модель статьи
    title = models.CharField('Название', max_length=500)
    created_at = models.DateTimeField('Дата публикации', auto_now_add=True)
    text = models.TextField('Текст', max_length=5000)
    image = models.ImageField(
        'Изображение',
        upload_to=get_path_upload_article_image,
        blank=True, 
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_image]
    )
    is_published = models.BooleanField('Опубликовано', default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='categories')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles')

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    def comments_count(self):
        return self.comments.count()

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']


class Comment(MPTTModel):
    # Модель комментария к статье
    text = models.TextField('Комментарий', max_length=500)
    created_at = models.DateTimeField('Дата комментария', auto_now_add=True)
    is_deleted = models.BooleanField('Удален', default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    parent = TreeForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children_comment'
    )

    def __str__(self):
        return '{} - {}'.format(self.user, self.article)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
