from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from blog.models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', context={"posts": posts})


def post_detail(request, pk):
    # post = get_object_or_404(Post, pk)
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', context={"post": post})
