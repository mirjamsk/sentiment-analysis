from rest_framework import serializers
from rest_framework import pagination
from .models import Post, Comment


class CustomPaginationSerializer(pagination.PageNumberPagination):
    max_page_size = 10
    last_page_strings = ('last',)
    page_size_query_param = 'limit'


class PostSerializer(serializers.ModelSerializer):
    detail_link = serializers.HyperlinkedIdentityField(view_name='post-detail')
    real_sentiment = serializers.JSONField(source='post_sentiment.real_sentiment')
    sentiment_api1_ol = serializers.JSONField(source='post_sentiment.sentiment_api1', read_only=True)
    sentiment_api1_en = serializers.JSONField(source='post_sentiment.sentiment_api1_en', read_only=True)
    sentiment_api2_ol = serializers.JSONField(source='post_sentiment.sentiment_api2', read_only=True)
    sentiment_api2_en = serializers.JSONField(source='post_sentiment.sentiment_api2_en', read_only=True)

    sentiment_api3 = serializers.JSONField(source='post_sentiment.sentiment_api3', read_only=True)
    sentiment_api4 = serializers.JSONField(source='post_sentiment.sentiment_api4', read_only=True)

    class Meta:
        model = Post
        related_fields = ['post_sentiment']
        fields = (
            'id',
            'detail_link',
            'content',
            'link',
            'likes',
            'shares',
            'comments',
            'real_sentiment',
            'sentiment_api1_ol',
            'sentiment_api1_en',
            'sentiment_api2_ol',
            'sentiment_api2_en',
            'sentiment_api3',
            'sentiment_api4',
        )
        read_only_fields = ('id', 'detail_link', 'content', 'link', 'likes', 'shares', 'comments')

    def update(self, instance, validated_data):
        # Handle related objects
        for related_obj_name in self.Meta.related_fields:

            # Validated data will show the nested structure
            data = validated_data.pop(related_obj_name)
            related_instance = getattr(instance, related_obj_name)

            # Same as default update implementation
            for attr_name, value in data.items():
                setattr(related_instance, attr_name, value)
            related_instance.save()
        return super(PostSerializer, self).update(instance, validated_data)


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    detail_link = serializers.HyperlinkedIdentityField(view_name='comment-detail')
    english_translation = serializers.CharField(source='comment_sentiment.english_translation', read_only=True)
    language = serializers.CharField(source='comment_sentiment.language', read_only=True)
    spam = serializers.JSONField(source='comment_sentiment.spam', read_only=True)

    real_sentiment = serializers.JSONField(source='comment_sentiment.real_sentiment')

    sentiment_api1_ol = serializers.JSONField(source='comment_sentiment.sentiment_api1', read_only=True)
    sentiment_api2_ol = serializers.JSONField(source='comment_sentiment.sentiment_api2', read_only=True)
    sentiment_api1_en = serializers.JSONField(source='comment_sentiment.sentiment_api1_en', read_only=True)
    sentiment_api2_en = serializers.JSONField(source='comment_sentiment.sentiment_api2_en', read_only=True)

    sentiment_api3 = serializers.JSONField(source='comment_sentiment.sentiment_api3', read_only=True)
    sentiment_api4 = serializers.JSONField(source='comment_sentiment.sentiment_api4', read_only=True)

    class Meta:
        model = Comment
        related_fields = ['comment_sentiment']
        fields = (
            'id',
            'language',
            'content',
            'english_translation',
            'real_sentiment',
            'sentiment_api1_ol',
            'sentiment_api1_en',
            'sentiment_api2_ol',
            'sentiment_api2_en',
            'sentiment_api3',
            'sentiment_api4',
            'spam',
            'idpost',
            'detail_link')
        read_only_fields = ('id', 'detail_link', 'idpost', 'content')

    def update(self, instance, validated_data):
        # Handle related objects
        for related_obj_name in self.Meta.related_fields:

            # Validated data will show the nested structure
            data = validated_data.pop(related_obj_name)
            related_instance = getattr(instance, related_obj_name)

            # Same as default update implementation
            for attr_name, value in data.items():
                setattr(related_instance, attr_name, value)
            related_instance.save()
        return super(CommentSerializer, self).update(instance, validated_data)
