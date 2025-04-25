from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('content', 'user__email', 'post__title')
    ordering = ('-created_at',)
