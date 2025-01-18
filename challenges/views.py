from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# def january(request):
#     """first views
#     """
#     return HttpResponse("Eat no meat for the entire month!")

# def february(request):
#     """month of feberary
#     """
#     return HttpResponse("Walke for at least 20 minutes every day!")

def months_challenge(request, month):
    """All months challenge.
    """
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meat for the entire month!"
    elif month == "february":
        challenge_text = "Walke for at least 20 minutes every day!"
    elif month == "march":
        challenge_text = "Learn Django for at least 20 minutes every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
