from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse("Hello World!")

def index(request):
    context = {'title': 'welcome', 'text': 'Hello!'}
    return render(request, 'blog/index.html', context)
