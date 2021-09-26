from django.conf.urls import url
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from django.views.generic import RedirectView

from .views import *
from . import views
from register import views as v
from django.contrib.auth import views as auth_views

# The URLS file handles routing on the website.
# EX. http://127.0.0.1:8000/discounts - will take you to the discounts page.
# Below you will see the URL patterns which do the routing for the website.
# testview is the initial page hence the path being a blank string '' - we should update this with the main homepage.


urlpatterns = [
    path('', index),
    path("register/", v.register, name="register"),
    path('discounts/', discounts),
    path('delivery_info/', delivery_info),
    path('events/', events),
    path('menu/', menu),
    path('order_confirmation/', order_confirmation),
    path('order_failure/', order_failure),
    path('orders/', all_products_view),
    path('payment_info/', payment_info),
    path('review_order/', review_order),
    path('about_us/', about_us),
    path('locations/', locations),
    path('orders/', views.orders, name='orders'),
    path('index/', views.index, name='index'),
    path('discounts/', views.discounts, name='discounts'),
    path('delivery_info/', views.delivery_info, name='delivery_info'),
    path('events/', events, name='events'),
    path('menu/', views.menu, name='menu'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('order_failure/', views.order_failure, name='order_failure'),
    path('payment_info/', payment_info, name='payment_info'),
    path('review_order/', views.review_order, name='review_order'),
    path('about_us/', views.about_us, name='about_us'),
    path('careers/', views.careers_view, name='careers'),
    path('locations/', views.locations, name='locations'),
    path('contact_us/', contactView, name='contact_us'),
    path('success/', successView, name='success'),
    path('submit/', submitView, name='submit'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('customer_entry_form/', views.customer_entry_form, name='customer_entry_form'),
    path('guest_or_user/', views.guest_or_user, name='guest_or_user'),
    path('update_item/', views.updateItem, name="update_item"),
    path('validate_username/', v.validate_username, name='validate_username'),
    path("favicon.ico",RedirectView.as_view(url=staticfiles_storage.url("pizzapp/images/icons/favicon.ico")),),
    path('pizza-delivery/', views.delivery, name='pizza-delivery'),
    path('payment/', views.payment, name='payment'),
    path('placeholder/', views.placeholder, name='placeholder'),
    path('cc_payment/', views.cc_payment, name='cc_payment'),
    path('cash_payment/', views.cash_payment, name='cash_payment'),
    path('charge_to_manager_payment/', views.charge_to_manager_payment, name='charge_to_manager_payment'),
    path('choose_location/', views.choose_location, name='choose_location'),
    path('get_location/', views.get_location, name='get_location'),
]
