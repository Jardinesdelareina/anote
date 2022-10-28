from rest_framework import serializers
from .._base.serializers import FilterCommentListSerializer, RecursiveSerializer
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


class CommentListSerializer(serializers.ModelSerializer):
    # Список комментариев
    text = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source='user.username')
    
    def get_text(self, obj):
        if obj.is_deleted:
            return None
        return obj.text

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = '__all__'


class CategoryArticleSerializer(serializers.ModelSerializer):
    # Категории статей
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    # Статья
    category = CategoryArticleSerializer(read_only=True)
    user = serializers.ReadOnlyField(source='user.username')
    comments = CommentListSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    # Список статей
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Article
        fields = '__all__'
