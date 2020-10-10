from django.shortcuts import render

# Create your views here.
from django.urls import path
from django.contrib.auth import views as auth_views

path('accounts/login/', auth_views.LoginView.as_view())