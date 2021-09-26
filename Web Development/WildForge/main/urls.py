from django.conf.urls import url
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from django.views.generic import RedirectView

from .views import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name="index")
]