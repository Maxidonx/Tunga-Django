from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, JsonResponse
from .models import Comment
from post.models import BlogPost

@login_required
def comment_create(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Comment.objects.create(post=post, user=request.user, content=content)
    return redirect("post-detail-page", post_id=post.id)

@login_required
def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('post-detail-page', post_id=comment.post.id)
    return render(request, 'comments/form.html', {'comment': comment, 'title': 'Edit Comment'})

@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user != request.user:
        return HttpResponseForbidden()
    post_id = comment.post.id
    if request.method == 'POST':
        comment.delete()
        return redirect('post-detail-page', post_id=post_id)
    return render(request, 'comments/delete.html', {'comment': comment})

@login_required
def comment_like_toggle(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
        liked = False
    else:
        comment.likes.add(request.user)
        liked = True
    return JsonResponse({'liked': liked, 'likes_count': comment.likes.count()})
