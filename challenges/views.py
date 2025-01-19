from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walke for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walke for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walke for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walke for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!"
}

# def january(request):
#     """first views
#     """
#     return HttpResponse("Eat no meat for the entire month!")

# def february(request):
#     """month of feberary
#     """
#     return HttpResponse("Walke for at least 20 minutes every day!")

def monthly_challenge_by_number(request, month):
    """months challenge by number.
    """
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def months_challenge(request, month):
    """All months challenge.
    """
    # challenge_text = None
    # if month == "january":
    #     challenge_text = "Eat no meat for the entire month!"
    # elif month == "february":
    #     challenge_text = "Walke for at least 20 minutes every day!"
    # elif month == "march":
    #     challenge_text = "Learn Django for at least 20 minutes every day!"
    # else:
    #     return HttpResponseNotFound("This month is not supported!")
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month not supported!")