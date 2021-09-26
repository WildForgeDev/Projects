from django.shortcuts import render
import decimal
import json
import random

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from main.functions import *
from .forms import *
from .models import *
from .models import *


def index(request):
    announcements = get_announcements()
    schedule_of_services = get_schedule_of_services()
    weekly_schedule = get_weekly_schedule()
    additional_announcements = get_additional_announcements()
    current_day = get_date()
    context = {"announcements": announcements,
               "schedule_of_services": schedule_of_services,
               "weekly_schedule": weekly_schedule,
               "additional_announcements": additional_announcements,
               "current_day": current_day}
    return render(request, "main/index.html", context)


def index_ru(request):
    announcements = get_announcements()
    schedule_of_services = get_schedule_of_services()
    weekly_schedule = get_weekly_schedule()
    additional_announcements = get_additional_announcements()
    current_day = get_date()
    context = {"announcements": announcements,
               "schedule_of_services": schedule_of_services,
               "weekly_schedule": weekly_schedule,
               "additional_announcements": additional_announcements,
               "current_day": current_day}
    return render(request, "main/index_ru.html", context)


def schedule_of_services(request):
    return render(request, "main/schedule_of_services.html")


def about_orthodox_faith(request):
    return render(request, "main/about_orthodox_faith.html")


def map_directions(request):
    return render(request, "main/map_directions.html")


def orthodox_calendar(request):
    return render(request, "main/orthodox_calendar.html")


def orthodox_way(request):
    return render(request, "main/orthodox_way.html")


def our_parish(request):
    return render(request, "main/our_parish.html")


def photo_gallery(request):
    return render(request, "main/photo_gallery.html")


def video_gallery(request):
    return render(request, "main/video_gallery.html")


def prayer_book(request):
    return render(request, "main/prayer_book.html")


def prayers(request):
    return render(request, "main/prayers.html")


def publications(request):
    return render(request, "main/publications.html")


def recommended_links(request):
    return render(request, "main/recommended_links.html")


def visitor_information(request):
    return render(request, "main/visitor_information.html")
