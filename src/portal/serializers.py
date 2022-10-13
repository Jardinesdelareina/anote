from xml.etree.ElementTree import Comment
from rest_framework import serializers
from .models import Category, Article


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
    user = serializers.ReadOnlyField(source='user.display_name')
    
    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text

    class Meta:
        model = Comment
        exclude = ('updated_at',)


class CategoryArticleSerializer(serializers.ModelSerializer):
    # Категории статей
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    # Статья
    category = CategoryArticleSerializer()
    user = serializers.ReadOnlyField(source='user.display_name')
    comments = CommentListSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    # Список статей
    user = serializers.ReadOnlyField(source='user.display_name')
    class Meta:
        model = Article
        fields = '__all__'
