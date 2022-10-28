from django.contrib import admin
from .models import Category, Article, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)
    ordering = ('title',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'is_published', 'created_at', 'user')
    list_filter = ('is_published',)
    list_display_links = ('title',)
    search_fields = ('title', 'text')
    ordering = ('-created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_at', 'user', 'article')
    list_filter = ('user', 'article')
    list_display_links = ('id',)
    ordering = ('-created_at',)
