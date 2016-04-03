from rest_framework import serializers
from .models import Post, Comment
from .utils import SENTIMENT_LABELS


class PostSerializer(serializers.ModelSerializer):
    detail_link = serializers.HyperlinkedIdentityField(view_name='post-detail')
    real_sentiment = serializers.ChoiceField(source='post_sentiment.real_sentiment', choices=SENTIMENT_LABELS)
    sentiment_api1 = serializers.CharField(source='post_sentiment.sentiment_api1', read_only=True)

    class Meta:
        model = Post
        related_fields = ['post_sentiment']
        fields = ('id', 'detail_link', 'content', 'link', 'likes', 'shares', 'comments', 'real_sentiment', 'sentiment_api1')
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
    real_sentiment = serializers.ChoiceField(source='comment_sentiment.real_sentiment', choices=SENTIMENT_LABELS)
    sentiment_api1 = serializers.CharField(source='comment_sentiment.sentiment_api1', read_only=True)
    sentiment_api2 = serializers.CharField(source='comment_sentiment.sentiment_api2', read_only=True)

    class Meta:
        model = Comment
        related_fields = ['comment_sentiment']
        fields = ('id', 'detail_link', 'idpost', 'content', 'real_sentiment', 'sentiment_api1','sentiment_api2')
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
