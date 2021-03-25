from django.shortcuts import render
from main.models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, "about.html")


def rooms(request):
    return render(request, 'rooms.html')


def owner(request):
    return render(request, 'owner.html')


def login(request):
    return render(request, 'login.html')
