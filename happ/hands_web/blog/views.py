from django.shortcuts import render

from .models import Post, Tag

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})

def post_detail(request, slug):
    post = Post.object.get(slug_iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post':post})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', context={'tags':tags})

def tag_detail(request, slug):
    tag = Tag.objects.get(slug_iexact=slug)
    return render(request, 'blog/tag_detail.html', context={'tag':tag})