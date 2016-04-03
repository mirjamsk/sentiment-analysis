from rest_framework import generics

from .serializers import PostSerializer, CommentSerializer, CommentSentimentSerializer
from .models import Post, Comment, CommentSentiment

# Create your views here.
# def index(request):
#    return HttpResponse("Hello, world! Bok bok")


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentSentimentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentSentiment.objects.all()
    serializer_class = CommentSentimentSerializer


