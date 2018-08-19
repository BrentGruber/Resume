from django.shortcuts import render

from .models import Post, Comment, EmbeddedImage

#TODO: how can I figure out the "popular posts?"


# Load a specific blog post
def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        images = EmbeddedImage.objects.get(post=post_id)
        print(images.image)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'blog/post.html', {'post': post})

#When a post is not found
def Not_Found(request):
    return render(request, 'blog/404.html')

#load all blog posts, make sure newest is first
#TODO: add pagination and search on the backend
def index(request):
    posts = Post.objects.all()
    context = {'posts': list(reversed(posts))}
    return render(request, 'blog/index.html', context)