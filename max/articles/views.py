from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    x =5

    return HttpResponse("<h1>MyClub Event Calendar</h1>")
