from django.shortcuts import render


# import HttpResponse from django.http
from django.http import HttpResponse

# import datetime to show today's date
from datetime import datetime


# Home view function
def home(request):
    return render(request, 'home/welcome.html', {'today' : datetime.today()})
