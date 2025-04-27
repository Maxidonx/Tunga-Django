# post/views_html.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.http import JsonResponse
from .models import BlogPost
from .forms import BlogPostForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

def blog_index(request):
    posts = BlogPost.objects.filter(is_published=True)
    return render(request, "post/index.html", {"posts": posts})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, "post/detail.html", {"post": post})


@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = BlogPostForm()
    return render(request, "post/form.html", {"form": form, "title": "Create Post"})

@login_required
def blog_edit(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/post/{post.id}/')
    else:
        form = BlogPostForm(instance=post)
    return render(request, "post/form.html", {"form": form, "title": "Edit Post"})

@login_required
def blog_delete(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect('/')
    return render(request, "post/delete.html", {"post": post})


@login_required
def post_like_toggle(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'liked': liked,
            'likes_count': post.likes.count()
        })
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
