from django.urls import path
from django_app import views

urlpatterns = [
    path('', views.djangoapp, name ='djangoapp'),
]