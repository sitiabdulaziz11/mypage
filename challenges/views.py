from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string  # for 404 we can use other approche

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
    # "december": "Learn Django for at least 20 minutes every day!"
    "december": None
}

# def january(request):
#     """first views
#     """
#     return HttpResponse("Eat no meat for the entire month!")

# def february(request):
#     """month of feberary
#     """
#     return HttpResponse("Walke for at least 20 minutes every day!")

def index(request):
    """views or function that cachs all urls.
    """
    # list_items = ""
    months = list(monthly_challenges.keys())  # list of months name.
    
    # for month in months:
    #     capitalized_month = month.capitalize()  # To capitaliz the first letter.
    #     month_path = reverse("month-challenge", args=[month])  # reverse is used to generate URLs dynamically from view names instead of hardcoding URL
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
        
        # "<li><a href="...">January</a></li> <li><a href="...">February</a></li>..."
    
    # response_data = """
    #     <ul>
    #         <li><a href="challenges/january">January</a></li>
    #     </ul>
    # """
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    
    return render(request, "challenges/index.html", {
        "month": months
    })

def monthly_challenge_by_number(request, month):
    """months challenge by number.
    """
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    # return HttpResponseRedirect("/challenges/" + redirect_month)
    
    redirect_path = reverse("month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


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
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            # "month_name": month.capitalize()  # to send dynamic content to html file.
            "month_name": month  # repleced by title in .html file.
            })  # This replace render_to_string, and render function requer request as a first argument to extract data enternally.
        # response_data = f"<h1>{challenge_text}</h1>"
        # response_data = render_to_string("challenges/challenge.html")  # to return html file
        # # return HttpResponse(challenge_text)
        # return HttpResponse(response_data)
    except:
        response_data = render_to_string("404.html")
        # # return HttpResponseNotFound("<h1>This month not supported!</h1>")
        return HttpResponseNotFound(response_data)
        
        # raise Http404()
