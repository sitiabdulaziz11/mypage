from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def january(request):
    """first views
    """
    return HttpResponse("Eat no meat for the entire month!")

def february(request):
    """month of feberary
    """
    return HttpResponse("Walke for at least 20 minutes every day!")
