from django.shortcuts import render, get_object_or_404
from .models import Post
def post_list(request):
    return render(request, "blog/list.html", {"posts": Post.objects.filter(is_published=True).order_by("-published_at")})
def post_detail(request, slug):
    return render(request, "blog/detail.html", {"post": get_object_or_404(Post, slug=slug, is_published=True)})
