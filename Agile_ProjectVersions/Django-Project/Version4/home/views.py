from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

#import login_required decoration from django
from django.contrib.auth.decorators import login_required


# Home view function
def home(request):
    return render(request, 'home/welcome.html', {'today' : datetime.today()})

# Authorized view
@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})
