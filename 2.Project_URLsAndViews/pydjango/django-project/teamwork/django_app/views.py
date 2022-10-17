from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def djangoapp(request):
    return HttpResponse("Welcome to Django App Page")