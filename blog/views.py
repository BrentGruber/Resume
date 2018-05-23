from django.shortcuts import render

from .models import Post, Comment


# Create your views here.
def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'blog/detail.html', {'post': post})