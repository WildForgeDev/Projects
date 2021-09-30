from django.conf.urls import url
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from django.views.generic import RedirectView

from .views import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name="index"),
    path('index_ru', index_ru, name="index_ru"),
    path('schedule_of_services/', schedule_of_services, name="schedule_of_services"),
    path('schedule_of_services_ru/', schedule_of_services_ru, name="schedule_of_services_ru"),
    path('about_orthodox_faith/', about_orthodox_faith, name="about_orthodox_faith"),
    path('map_directions/', map_directions, name="map_directions"),
    path('orthodox_calendar/', orthodox_calendar, name="orthodox_calendar"),
    path('orthodox_way/', orthodox_way, name="orthodox_way"),
    path('our_parish/', our_parish, name="our_parish"),
    path('photo_gallery/', photo_gallery, name="photo_gallery"),
    path('video_gallery/', video_gallery, name="video_gallery"),
    path('prayer_book/', prayer_book, name="prayer_book"),
    path('prayers/', prayers, name="prayers"),
    path('publications/', publications, name="publications"),
    path('recommended_links/', recommended_links, name="recommended_links"),
    path('visitor_information/', visitor_information, name="visitor_information"),
    path('prayer_book/', prayer_book, name="prayer_book"),
]
