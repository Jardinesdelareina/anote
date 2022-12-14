from rest_framework import serializers
from ..utils.serializers import FilterCommentListSerializer, RecursiveSerializer
from .models import Category, Article, Comment


class CommentCreateSerializer(serializers.ModelSerializer):
    # Создание комментария
    class Meta:
        model = Comment
        fields = (
            'article',
            'text',
            'parent',
        )


class CommentSerializer(serializers.ModelSerializer):
    # Список комментариев
    text = serializers.SerializerMethodField()
    children_comment = RecursiveSerializer(many=True)
    user = serializers.ReadOnlyField(source='user.username')
    
    def get_text(self, obj):
        if obj.is_deleted:
            return None
        return obj.text

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = (
            'id',
            'article',
            'user',
            'text',
            'created_at',
            'children_comment',
        )


class CategorySerializer(serializers.ModelSerializer):
    # Категории статей
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    # Статья
    user = serializers.ReadOnlyField(source='user.username')
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'created_at',
            'text',
            'image',
            'category',
            'user',
            'comments',
        )


class ArticleListSerializer(serializers.ModelSerializer):
    # Статья
    category = CategorySerializer()
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'created_at',
            'image',
            'category',
            'user',
            'comments_count',
        )
