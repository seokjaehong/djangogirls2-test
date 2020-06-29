from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from blog.forms import PostForm
from blog.models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', context={"posts": posts})


def post_detail(request, pk):
    # post = get_object_or_404(Post, pk)
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', context={"post": post})


def post_edit(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk)
    # print(request.method)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
