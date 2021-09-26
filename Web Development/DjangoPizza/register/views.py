from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from pizzapp.models import Customer, User
from .forms import RegisterForm
import random
from django.http import JsonResponse


def index(request):
    if request.session.is_empty():
        request.session["visitor_id"] = random.randint(10000000, 99999999)
    return render(request, "pizzapp/index.html")


def register(request):
    if request.user.is_authenticated:
        return redirect('/orders')
    else:
        if request.session.is_empty():
            request.session["visitor_id"] = random.randint(10000000, 99999999)
        if request.method == 'POST':
            user_form = RegisterForm(request.POST)
            if user_form.is_valid():
                new_customer = Customer()
                username = user_form.cleaned_data.get('username')
                new_customer.delivery_type = user_form.cleaned_data['delivery_type']
                new_customer.first_name = user_form.cleaned_data['first_name']
                new_customer.last_name = user_form.cleaned_data['last_name']
                new_customer.address = user_form.cleaned_data['address']
                new_customer.city = user_form.cleaned_data['city']
                new_customer.state = user_form.cleaned_data['state']
                new_customer.zip_code = user_form.cleaned_data['zip_code']
                new_customer.phone_number = user_form.cleaned_data['phone_number']
                new_customer.email = user_form.cleaned_data['email']
                visitor_id = request.session["visitor_id"]
                new_customer.visitor_id = visitor_id
                user_form.save()
                new_user = User.objects.get(username=username)
                new_user_id = new_user.pk
                request.session["user_id"] = new_user_id
                new_customer.user_id = new_user_id
                Customer.save(new_customer)
                raw_password = user_form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
            return redirect('/orders')
        else:
            user_form = RegisterForm()
            context = {
                "user_form": user_form
            }
            return render(request, 'register/register.html', context)

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)