# post/views.py
from rest_framework import viewsets, permissions
from .models import BlogPost
from .serializers import BlogPostSerializer, BlogPostDetailSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BlogPostDetailSerializer
        return BlogPostSerializer

    @swagger_auto_schema(
        operation_description="Create a new blog post",
        responses={201: BlogPostSerializer},
        request_body=BlogPostSerializer
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="List all blog posts",
        responses={200: BlogPostSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retrieve a blog post by ID",
        responses={200: BlogPostDetailSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
