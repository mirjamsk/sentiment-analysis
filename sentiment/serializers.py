from rest_framework import serializers
from .models import Post, Comment, PostSentiment, CommentSentiment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'content', 'link', 'likes', 'shares', 'comments')


class PostSentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostSentiment
        fields = ('id', 'idpost', 'sentiment', 'real_sentiment')


class CommentSentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentSentiment
        fields = ('id', 'idpost', 'idcomment', 'sentiment', 'real_sentiment')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'idpost','content')


