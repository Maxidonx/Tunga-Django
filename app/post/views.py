from rest_framework import viewsets, permissions
from .models import BlogPost
from .serializers import BlogPostSerializer, BlogPostDetailSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BlogPostDetailSerializer
        return BlogPostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
