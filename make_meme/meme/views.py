from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, 'meme/home.html')

def about(request):
    return render(request, 'meme/about.html')

def technology(request):
    return render(request, 'meme/technology.html')

def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'meme/blog.html', context)

# Create your views here.
