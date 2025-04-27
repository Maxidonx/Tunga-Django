from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'nationality', 'profile_picture', 'cover_photo', 'bio', 'linkedin', 'facebook', 'twitter', 'instagram']

