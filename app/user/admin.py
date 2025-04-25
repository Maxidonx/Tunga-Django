from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'user', 'nationality')
    search_fields = ('user__email', 'first_name', 'last_name')
    ordering = ('first_name',)
