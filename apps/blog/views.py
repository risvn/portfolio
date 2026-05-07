from django.shortcuts import render

posts = [
    {
        "title": "Building a Local AI Voice Assistant",
        "date_posted": "2026-05-07",
        "author": "Wan",
        "description": "Created a real-time voice assistant using llama.cpp, Whisper.cpp, and Piper TTS running on Raspberry Pi.",
        "location": "Hyderabad, India"
    },
    {
        "title": "My Experience Switching to Fedora",
        "date_posted": "2026-04-28",
        "author": "Aarav Sharma",
        "description": "After years on Windows, I moved to Fedora for development and customization. Here’s what changed.",
        "location": "Bengaluru, India"
    },
    {
        "title": "Deploying Django with Nginx",
        "date_posted": "2026-04-19",
        "author": "Fatima Khan",
        "description": "Step-by-step guide to deploying a Django application using Gunicorn and Nginx on Ubuntu.",
        "location": "Mumbai, India"
    },
    {
        "title": "Learning Low-Level Programming in C",
        "date_posted": "2026-04-10",
        "author": "Rohan Patel",
        "description": "Understanding pointers, memory management, and system calls while building terminal utilities.",
        "location": "Pune, India"
    }
]


def home(request):
    context = {
        "message": "Welcome to my portfolio",
        "posts": posts
    }

    return render(request, "blog/home.html", context)

