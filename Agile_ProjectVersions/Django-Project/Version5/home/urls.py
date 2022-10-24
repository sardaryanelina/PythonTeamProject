from django.urls import path

# import views from "home" folder
from . import views

urlpatterns = [
    path('home', views.HomeView.as_view()),
    path('authorized', views.AuthorizedView.as_view()),
]