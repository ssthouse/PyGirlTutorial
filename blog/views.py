from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    print("**************************")
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    form = PostForm()
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    return render(request, 'blog/post_edit.html', {'form': form})
