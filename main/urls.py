
from django.urls import path
from main.views import *
urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('about', about, name='about'),
    path('room', rooms, name='rooms'),
    path('owner', owner, name='owner')
]
