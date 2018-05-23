from django.shortcuts import render

from .models import Post, Comment


# Create your views here.
def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'blog/post.html', {'post': post})

def Not_Found(request):
    return render(request, 'blog/404.html')

def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)