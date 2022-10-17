from django.urls import path
from django_app import views

urlpatterns = [
    path('', views.djangoapp, name ='djangoapp'),
     path('contact-us', views.contact, name ='contact'),
      path('about-us', views.about, name ='about'),
]