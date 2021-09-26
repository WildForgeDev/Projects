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

from pizzapp.functions import *
from .forms import ContactForm, CustomerForm, CareersForm
from .models import Product, ProductTypes, Customer, Order, Cart, Careers, Payments, Payment_Details, Promo_Code_Payment
from .models import Cash_Payment


# Create your views here.

# This view function returns the homepage and checks to see if there is a visitor session id set and if one does not
# exist it creates one.
def index(request):
    if request.session.is_empty():
        request.session["visitor_id"] = random.randint(10000000, 99999999)
    return render(request, "pizzapp/index.html")


# This view is used for the initial page before going to the order page that asks if you want to continue as a guest,
# login, or create an account. It gets the visitor id from the stored session, then tries to get the existing guest
# id for the customer and if it does not get an existing customer id it asks you to continue as guest or login etc.
# If it gets an existing customer id it takes directly to the order page to continue the order.
def guest_or_user(request):
    visitorid = request.session["visitor_id"]
    try:
        existing_guest_customer = Customer.objects.get(visitor_id=visitorid)
    except ObjectDoesNotExist:
        return render(request, "pizzapp/guest_or_user.html")
    if Order.objects.filter(customer_id=existing_guest_customer.pk).exists():
        return redirect('/orders')
    if request.user.is_authenticated:
        return redirect('/orders')
    else:
        return render(request, "pizzapp/guest_or_user.html")


# This renders the discount page
def discounts(request):
    return render(request, "pizzapp/discounts.html")


# This renders the delivery info page
def delivery_info(request):
    return render(request, "pizzapp/delivery_info.html")


# This renders the events page
def events(request):
    return render(request, "pizzapp/events.html")


# This renders the menu page
def menu(request):
    return render(request, "pizzapp/menu.html")


# This renders the order confirmation page
def order_confirmation(request):
    existing_customer = get_existing_customer_record(request)
    existing_order = get_existing_order_record(existing_customer)
    delivery_type = get_delivery_type(existing_order)
    payment_name = get_payment_type(existing_order)
    getcart = Cart.objects.filter(order_id=existing_order.pk)
    context = {"getcart": getcart,
               "existing_order": existing_order,
               "existing_customer": existing_customer,
               "payment_name": payment_name}
    return render(request, "pizzapp/order_confirmation.html", context)


# This renders the order failure page
def order_failure(request):
    return render(request, "pizzapp/order_failure.html")


# This renders the orders page
def orders(request):
    return render(request, "pizzapp/orders.html")


# This renders the payment info page
def payment_info(request):
    return render(request, "pizzapp/payment_info.html")


# This renders the review order page. It is similar to the all products view in that we check if the user is
# authenticated or not and return an existing order from that proess, then we use tht existing order to get the cart and
# return that data to the html page.
def review_order(request):
    existing_order = '1'
    if request.user.is_authenticated:
        existing_user_id = request.user
        existing_customer = Customer.objects.get(user_id=existing_user_id)
        existing_order = Order.objects.get(customer_id=existing_customer.pk)
    if not request.user.is_authenticated:
        visitorid = request.session["visitor_id"]
        existing_guest_customer = Customer.objects.get(visitor_id=visitorid)
        existing_order = Order.objects.get(customer_id=existing_guest_customer.pk)
    getcart = Cart.objects.filter(order_id=existing_order.pk)
    context = {"getcart": getcart,
               "existing_order": existing_order}
    return render(request, "pizzapp/review_order.html", context)


# This renders the login page
def Login(request):
    return render(request, "registration/login.html")


# This renders the about us page
def about_us(request):
    return render(request, "pizzapp/about_us.html")


# This renders the locations page
def locations(request):
    return render(request, "pizzapp/locations.html")


# This renders the order page. It starts by checking if the user is authenticated and sets the existing order id with
# that data. if there is not an existing order it creates one. We pass in the get cart query to get the current cart
# data to render if there is any. We also return all the menu product data to render the menu options to add to the
# cart. We then put all that data from the databse and pass it to the order views.
def all_products_view(request):
    print(request.user)
    # quantity_form = QuantityForm()
    existing_order = None
    if request.user.is_authenticated:
        existing_user_id = request.user
        existing_customer = Customer.objects.get(user_id=existing_user_id)
        if Order.objects.filter(customer_id=existing_customer.pk).exists():
            existing_order = Order.objects.get(customer_id=existing_customer.pk)
        else:
            new_order = Order()
            new_order.order_type_id = existing_customer.delivery_type
            new_order.customer_id = existing_customer.pk
            new_order.order_completed = 0
            new_order.delivery_fee = 0
            new_order.location_id = None
            Order.save(new_order)
            existing_order = Order.objects.get(customer_id=existing_customer.pk)
    if not request.user.is_authenticated:
        visitorid = request.session["visitor_id"]
        existing_guest_customer = Customer.objects.get(visitor_id=visitorid)
        if Order.objects.filter(customer_id=existing_guest_customer.pk).exists():
            existing_order = Order.objects.get(customer_id=existing_guest_customer.pk)
        else:
            new_order = Order()
            new_order.order_type_id = existing_guest_customer.delivery_type
            new_order.customer_id = existing_guest_customer.pk
            new_order.order_completed = 0
            new_order.delivery_fee = 0
            new_order.location_id = None
            Order.save(new_order)
            existing_order = Order.objects.get(customer_id=existing_guest_customer.pk)
    getcart = Cart.objects.filter(order_id=existing_order.pk)
    allproducts = Product.objects.all()
    menu_categories = ProductTypes.objects.all()
    context = {"allproducts": allproducts, "menu_categories": menu_categories, "getcart": getcart,
               "existing_order": existing_order}
    return render(request, "pizzapp/orders.html", context)


# This renders the contact us page
def contact_us(request):
    return render(request, "pizzapp/contact_us.html")


# This renders the contact us page
def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "pizzapp/contact_us.html", {'form': form})


# This renders the success page. I am not sure what this does.
def successView(request):
    return render(request, "pizzapp/success.html")


# This renders the careers view.
def careers_view(request):
    career_form = CareersForm()
    if request.method == "POST":
        career_form = CareersForm(request.POST)
        if career_form.is_valid():
            new_career = Careers()
            new_career.position = career_form.cleaned_data['position']
            new_career.first_name = career_form.cleaned_data['first_name']
            new_career.last_name = career_form.cleaned_data['last_name']
            new_career.from_email = career_form.cleaned_data['from_email']
            new_career.phone_number = career_form.cleaned_data['phone_number']
            new_career.resume = career_form.cleaned_data['resume']
            Careers.save(new_career)
            return redirect('/submit/')
        else:
            print(career_form.errors)
    context = {
        "form": career_form
    }
    return render(request, "pizzapp/careers.html", context)


# This renders the submit page
def submitView(request):
    return render(request, "pizzapp/submit.html")


# # This renders the user login page. I didn't write this part so we need to add comments here.
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('orders')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login": form})


# This renders the customer entry form page which is the form that allows us to log in as a guest or rather create
# an order as a guest.
def customer_entry_form(request):
    if request.session.is_empty():
        request.session["visitor_id"] = random.randint(10000000, 99999999)
    customer_form = CustomerForm()
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            visitor_id = request.session["visitor_id"]
            newdata = {'visitor_id': visitor_id}
            testdata = customer_form.cleaned_data
            testdata.update(newdata)
            print(testdata)
            Customer.objects.create(**testdata)
            return redirect('/orders')
        else:
            print(customer_form.errors)
    context = {
        "form": customer_form
    }
    return render(request, "pizzapp/customer_entry_form.html", context)


# This is the main function that powers the orders and confirm orders page. What we are doing here is using the
# functions in functions.py to go through thee flow of adding data to the cart or remove data from the cart. If you
# need to understand this function look at functions.py to see what  each function is doing over there. In this
# function we are passing in the data from the functions there into the functions there to move data around and perform
# calculations on the data. First we load any Ajax requests from the app.js file which is essentially using a post
# request to send data to the view here and use that data to update the page in javascript without having to refresh
# the page. Ajax stands for asynchronous Javascript. That means we send post requests to our server and the view code
# exists outside the front end code from the HTML and Javascript. Once we pass this data we can use it in the view to
# add and remove records from the database. This is helpful to us because we don't expose any of the data to the front
# end and risk user data. Anyway we get the data from the page we are rendering for the user and we use that data to
# update the html pages for orders and order confirmation. To be brief the post request from Javascript get sent to
# the updateitem endpoint here to run this code whenever the server detects the Javascript sending a post request. You
# can see this in app.js by looking for the keyword AJAX and then you can see the data we are pulling from the HTML
# into the javascript to send to the server here. These functions update the database and that is how we create an order.
def updateItem(request):
    data = json.loads(request.body)
    action = data['action']
    product_query = get_product_data(action, data)
    existing_customer = get_existing_customer_record(request)
    existing_order = get_existing_order_record(existing_customer)
    quantity = decimal.Decimal(float(1.0))
    price = product_query.price
    total_price = price * quantity
    item_id = product_query.pk
    order_id = existing_order.pk
    cart_item = None
    product_name = None
    if action == 'add':
        product_picture = product_query.image
        product_name = product_query.name
        cart_item = create_cart_object(quantity, price, item_id, order_id, product_name, total_price, product_picture)
    if action == 'remove':
        product_name = product_query.product_name
        cart_item = data['cart_id']
    cart_query = get_cart(cart_item)
    new_subtotal = update_order_subtotal(action, existing_order, cart_query)
    new_delivery_fee = update_order_delivery_fee(action, existing_order, cart_query)
    new_tax = update_order_tax(existing_order, action, cart_query)
    new_grand_total = update_order_grand_total(existing_order, action, cart_query)
    existing_order.tax = new_tax
    existing_order.delivery_fee = new_delivery_fee
    existing_order.subtotal = new_subtotal
    existing_order.grand_total = new_grand_total
    existing_order.save()
    data = {'order_subtotal': new_subtotal, 'order_delivery_fee': new_delivery_fee, 'order_tax': new_tax,
            'order_grand_total': new_grand_total, 'product_name': product_name, 'cart_id': cart_item}
    cart_update_handler(action, cart_query)
    return JsonResponse(data, safe=False)


def delivery(request):
    return render(request, "pizzapp/pizza-delivery.html")


# This is a placeholder page for testing while I work on the payment system.
def placeholder(request):
    return render(request, "pizzapp/placeholder.html")


# This renders the basic choose location page
def choose_location(request):
    return render(request, "pizzapp/choose_location.html")


def get_location(request):
    if request.method == 'POST':
        location = request.POST['location']
        existing_customer = get_existing_customer_record(request)
        existing_order = get_existing_order_record(existing_customer)
        getcart = Cart.objects.filter(order_id=existing_order.pk)
        cart_item_number = getcart.count()
        existing_order.location_id = location
        existing_order.save()
        context = {"getcart": getcart,
                   "existing_order": existing_order,
                   "cart_item_number": cart_item_number}
        return render(request, "pizzapp/payment.html", context)


# This method below is going to allows us to pull the delivery type for the customer and redirect to the location
# picker page or directly to the payment page.
def payment(request):
    existing_customer = get_existing_customer_record(request)
    existing_order = get_existing_order_record(existing_customer)
    delivery_type = get_delivery_type(existing_order)
    getcart = Cart.objects.filter(order_id=existing_order.pk)
    cart_item_number = getcart.count()
    print(cart_item_number)
    if delivery_type == 1:
        context = {"getcart": getcart,
                   "existing_order": existing_order,
                   "cart_item_number": cart_item_number}
        return render(request, "pizzapp/payment.html", context)
    else:
        all_locations = get_locations()
        context = {"all_locations": all_locations}
        return render(request, "pizzapp/choose_location.html", context)


# This function is to get the CC payment details when a customer submits a CC payment in the payment section.
def cc_payment(request):
    if request.method == 'POST':
        billing_name = request.POST['billing_name']
        billing_email = request.POST['billing_email']
        billing_address = request.POST['billing_address']
        billing_city = request.POST['billing_city']
        billing_state = request.POST['billing_state']
        billing_zip = request.POST['billing_zip']
        billing_cc_name = request.POST['billing_cc_name']
        billing_cc_number = request.POST['billing_cc_number']
        billing_exp_month = request.POST['billing_exp_month']
        billing_exp_year = request.POST['billing_exp_year']
        billing_cvv = request.POST['billing_cvv']
        existing_customer = get_existing_customer_record(request)
        existing_order = get_existing_order_record(existing_customer)
        payment_total = existing_order.grand_total
        customer_number = existing_customer.pk
        order_number = existing_order.pk
        getcart = Cart.objects.filter(order_id=existing_order.pk)
        payment_type = 2
        new_payment = Payments()
        new_payment.payment_total = payment_total
        new_payment.customer_number_id = customer_number
        new_payment.order_number_id = order_number
        new_payment.payment_types_id = payment_type
        new_payment.save()
        new_payment_details = Payment_Details()
        new_payment_details.customer_name = billing_name
        new_payment_details.billing_email = billing_email
        new_payment_details.billing_address = billing_address
        new_payment_details.billing_city = billing_city
        new_payment_details.billing_state = billing_state
        new_payment_details.billing_zip = billing_zip
        new_payment_details.customer_name = billing_cc_name
        new_payment_details.credit_card_number = billing_cc_number
        new_payment_details.expiration_month = billing_exp_month
        new_payment_details.expiration_year = billing_exp_year
        new_payment_details.security_code = billing_cvv
        new_payment_details.payment_id = new_payment.pk
        new_payment.payment_type_id = 2
        new_payment_details.save()
        payment_name = get_payment_type(existing_order)
        context = {"getcart": getcart,
                   "existing_order": existing_order,
                   "existing_customer": existing_customer,
                   "payment_name": payment_name}
        return render(request, "pizzapp/order_confirmation.html", context)


def charge_to_manager_payment(request):
    if request.method == 'POST':
        promo_code_used = request.POST['promo-code']
        existing_customer = get_existing_customer_record(request)
        existing_order = get_existing_order_record(existing_customer)
        getcart = Cart.objects.filter(order_id=existing_order.pk)
        payment_total = existing_order.grand_total
        customer_number = existing_customer.pk
        order_number = existing_order.pk
        payment_type = 3
        new_payment = Payments()
        new_payment.payment_total = payment_total
        new_payment.customer_number_id = customer_number
        new_payment.order_number_id = order_number
        new_payment.payment_types_id = payment_type
        new_payment.save()
        new_promo_payment = Promo_Code_Payment()
        new_promo_payment.promo_code_used = promo_code_used
        new_promo_payment.payment_id = new_payment.pk
        new_promo_payment.save()
        payment_name = get_payment_type(existing_order)
        context = {"getcart": getcart,
                   "existing_order": existing_order,
                   "existing_customer": existing_customer,
                   "payment_name": payment_name}
        return render(request, "pizzapp/order_confirmation.html", context)


def cash_payment(request):
    if request.method == 'POST':
        existing_customer = get_existing_customer_record(request)
        existing_order = get_existing_order_record(existing_customer)
        getcart = Cart.objects.filter(order_id=existing_order.pk)
        payment_type = 1
        payment_total = existing_order.grand_total
        customer_number = existing_customer.pk
        order_number = existing_order.pk
        new_payment = Payments()
        new_payment.payment_total = payment_total
        new_payment.customer_number_id = customer_number
        new_payment.order_number_id = order_number
        new_payment.payment_type_id = payment_type
        new_payment.save()
        new_cash_payment = Cash_Payment()
        new_cash_payment.payment_id = new_payment.pk
        new_cash_payment.save()
        payment_name = get_payment_type(existing_order)
        context = {"getcart": getcart,
                   "existing_order": existing_order,
                   "existing_customer": existing_customer,
                   "payment_name": payment_name}
        return render(request, "pizzapp/order_confirmation.html", context)
