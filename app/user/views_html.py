from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm

@login_required
def profile_edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-page')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'user/profile_form.html', {'form': form, 'title': 'Edit Profile'})

@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'user/profile.html', {'profile': profile})
