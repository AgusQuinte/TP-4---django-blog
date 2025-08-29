# blog/views.py

from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post).order_by("-created_on")

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            return redirect("blog:detail", pk=post.pk)
    else:
        form = CommentForm()

    return render(request, "blog/detail.html", {
        "post": post,
        "comments": comments,
        "form": form,
    })