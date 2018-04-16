from rest_framework import serializers
from bot.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'author', 'ups', 'num_comments', 'created_at')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author',)
