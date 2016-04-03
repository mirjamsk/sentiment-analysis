from rest_framework import serializers
from .models import Post, Comment
from .utils import SENTIMENT_LABELS


class PostSerializer(serializers.ModelSerializer):
    real_sentiment = serializers.ChoiceField(source='post_sentiment.real_sentiment', choices=SENTIMENT_LABELS)
    sentiment_api1 = serializers.CharField(source='post_sentiment.sentiment_api1', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'content', 'link', 'likes', 'shares', 'comments', 'real_sentiment', 'sentiment_api1')
        related_fields = ['post_sentiment']
        read_only_fields = ('id', 'content', 'link', 'likes', 'shares', 'comments')

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
    real_sentiment = serializers.ChoiceField(source='comment_sentiment.real_sentiment', choices=SENTIMENT_LABELS)
    sentiment_api1 = serializers.CharField(source='comment_sentiment.sentiment_api1', read_only=True)

    class Meta:
        model = Comment
        related_fields = ['comment_sentiment']
        fields = ('id', 'idpost', 'content', 'real_sentiment', 'sentiment_api1')
        read_only_fields = ('id', 'idpost', 'content')

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
