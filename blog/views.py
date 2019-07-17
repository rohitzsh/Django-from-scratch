from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return render(request, "<h1>Test</h1>", {})

def index(request):
    return HttpResponse("<h1>This is a custom response</h1>")

def post(request, postid):
    output="post ID: %s"%postid
    return HttpResponse(output)