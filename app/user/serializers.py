from rest_framework import serializers
from .models import UserProfile
from register.serializers import CustomUserSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'first_name', 'last_name', 'nationality', 'profile_picture']
