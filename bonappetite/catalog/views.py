from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def user_profile(request, user_id):
    return HttpResponse("You can manage your profile here. UserId = %s" % user_id)


def recipes(request):
    return HttpResponse("Recipes board here")
