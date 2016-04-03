from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment

# Create your views here.
#def index(request):
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
