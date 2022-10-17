from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def djangoapp(request):
    # return HttpResponse("Welcome to Django App Page")
    context = {'welcome_text':"Welcome to our website!"}
    return render(request, 'project.html', context)

def contact(request):
    # return HttpResponse("Welcome to Django App Page")
    context = {'contact_text':"Welcome to contact page."}
    return render(request, 'contact.html', context)

def about(request):
    # return HttpResponse("Welcome to Django App Page")
    context = {'about_text':"Welcome to about page."}
    return render(request, 'about.html', context)