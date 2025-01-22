from django.urls import path

from . import views

urlpatterns = [
    # path("january", views.january),
    # path("february", views.february),
    path("", views.index),  # /challenges/
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.months_challenge, name="month-challenge")
]
