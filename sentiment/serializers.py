from rest_framework import serializers
from .models import Post, Comment, PostSentiment, CommentSentiment


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'content', 'link', 'likes', 'shares', 'comments')


class PostSentimentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostSentiment
        fields = ('id', 'idpost', 'sentiment', 'real_sentiment')


class CommentSentimentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommentSentiment
        fields = ('id', 'idpost', 'idcomment', 'sentiment', 'real_sentiment')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'idpost','content')


