from rest_framework import serializers
from .models import ImPost, ImComment

class ImPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImPost
        fields = ('id', 'content', 'link', 'likes', 'shares', 'comments')


class ImCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImComment
        fields = ('id', 'idpost','content')
