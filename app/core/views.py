from django.shortcuts import render
from post.models import BlogPost

def dashboard(request):
    all_posts = BlogPost.objects.filter(is_published=True)
    if request.user.is_authenticated:
        my_posts = all_posts.filter(author=request.user)
        other_posts = all_posts.exclude(author=request.user)
        return render(request, "core/dashboard.html", {
            "my_posts": my_posts,
            "other_posts": other_posts,
        })
    return render(request, "core/landing.html", {"posts": all_posts})
