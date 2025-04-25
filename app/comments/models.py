from django.db import models
from django.conf import settings

class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments'
    )
    post = models.ForeignKey(
        'post.BlogPost', on_delete=models.CASCADE, related_name='comments'
    )
    content = models.TextField()
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_comments', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.email} on {self.post.title}"

    class Meta:
        ordering = ['-created_at']
