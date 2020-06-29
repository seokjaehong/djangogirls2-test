from django.shortcuts import render

# Create your views here.
from blog.models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', context={"posts": posts})
