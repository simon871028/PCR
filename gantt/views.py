from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    s = "Hello World!"
    return HttpResponse(s)