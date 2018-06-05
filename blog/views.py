from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def post_list(request):
    return render(request, 'blog/post_list.html', {})

def cripto_app(request):
    return render(request, 'cripto/main.html', {})

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

def git_guide(request):
    return render(request, 'blog/git_usage.html', {})