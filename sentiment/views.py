from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializers import ImPostSerializer, ImCommentSerializer
from .models import ImPost, ImComment

# Create your views here.
#def index(request):
#    return HttpResponse("Hello, world! Bok bok")


class ImPostList(generics.ListCreateAPIView):
    queryset = ImPost.objects.all()
    serializer_class = ImPostSerializer

class ImPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImPost.objects.all()
    serializer_class = ImPostSerializer

class ImCommentList(generics.ListCreateAPIView):
    queryset = ImComment.objects.all()
    serializer_class = ImCommentSerializer

class ImCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImComment.objects.all()
    serializer_class = ImCommentSerializer
