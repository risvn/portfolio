from django.shortcuts import render
from .models import Post



def home(request):
    posts = Post.objects.all()
    context = {
        "message": "Welcome to my portfolio",
        "posts": posts
    }

    return render(request, "blog/home.html", context)

