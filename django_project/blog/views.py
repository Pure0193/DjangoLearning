from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'First Guy',
        'title': 'Blog Number 1',
        'content': 'First is HERE!',
        'date_posted': 'June 1, 2023'
    },
    {
        'author': 'Second Girl',
        'title': 'Blog Number 2',
        'content': 'I\'m here too!',
        'date_posted': 'June 2, 2023'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {'title': 'About'})