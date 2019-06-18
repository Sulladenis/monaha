from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BlogPhoto, Blog


def index(request):
    post = Blog.objects.get(pk=1)
    imgs = BlogPhoto.objects.filter(post=post)
    return render(request, 'blog/index.html', context={'post': post, 'imgs': imgs})
