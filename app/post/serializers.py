from rest_framework import serializers
from .models import BlogPost
from register.serializers import CustomUserSerializer
from comments.serializers import CommentSerializer  # optional

class BlogPostSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'author', 'title', 'content', 'image', 'created_at', 'updated_at', 'is_published']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']


class BlogPostDetailSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'is_published', 'comments']
