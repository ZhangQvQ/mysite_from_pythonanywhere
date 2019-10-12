from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("Hello world!")

def index(request):
    context_dict = {'text': "Hello World!",}
    response = render(request, 'avgle/index.html', context=context_dict)
    return response
