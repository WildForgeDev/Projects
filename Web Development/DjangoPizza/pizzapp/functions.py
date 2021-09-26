import decimal
from .models import Product, Customer, Order, Cart, Locations, Payments, Payment_Types


# This function is recieving the request from the update cart view and checking if they are logged in.
# This way we can use this function inside of our views to easily see if the user is logged in.
def user_auth_check(request):
    auth_status = False
    if request.user.is_authenticated:
        auth_status = True
    return auth_status


# This function is taking in the cart item id from our Ajax request in Javascript ad plugging that into the cart query
# The cart query is pulling the specific cart record that matches the primary key in the table.
# cart_item = cart primary key
def get_cart(cart_item):
    cart_query = Cart.objects.get(pk=cart_item)
    return cart_query

# This function is a handler for the type of update we are doing to the cart.
# Starting in our Javascript, depending on what button you press it sends the update type to the View
# Using this function we can return what type of update we are doing to the cart and conditionally choose what action
# will proceed that action. This function takes the cart_query array and the action from the javascript Ajax call
# as inputs.
def cart_update_handler(action, cart_query):
    if action == "add":
        print("Cart item exists, no action needed")
    if action == "remove":
        cart_query.delete()


# This function is returning data about a specific product we are adding to the cart.
# It takes the action (add or remove) from the Ajax call from Javascript and the product data from the Javascript
# If the action is remove it gets the cart id in order to return the cart and remove the idem from the database.
# If the action is add it returns data on the product.
def get_product_data(action, data):
    if action == 'add':
        product_id = data['productId']
        product_query = Product.objects.get(pk=product_id)
        return product_query
    if action == 'remove':
        cart_id = data['cart_id']
        cart_query = Cart.objects.get(pk=cart_id)
        return cart_query


# This function gets the existing customer record by taking in the request from the view and depending on if the request
# returns authenticated or not it sets the existing customer variable as the primary key for the user or as the visitor
# id for the user. This can be used to determine if the user is authenticated on the fly.
def get_existing_customer_record(request):
    existing_user_id = request.user
    if request.user.is_authenticated:
        existing_customer = Customer.objects.get(user_id=existing_user_id)
    else:
        visitor_id = request.session['visitor_id']
        existing_customer = Customer.objects.get(visitor_id=visitor_id)
    return existing_customer


# This function gets the existing order record meaning the database record and returns the data as an array to use that
# that data. It takes the existing customer id or primary key which can be obtained through another one of the functions
# in this file.
def get_existing_order_record(existing_customer):
    existing_order = Order.objects.get(customer_id=existing_customer.pk)
    return existing_order


# This function is used to create a cart object meaning a cart record in the cart table of the database. We pass in the
# quantity, price, item_id, order_id, product_name, total_price, product_picture and save the record to create it in the
# database.
def create_cart_object(quantity, price, item_id, order_id, product_name, total_price, product_picture):
    new_cart_item = Cart()
    new_cart_item.quantity = quantity
    new_cart_item.price = price
    new_cart_item.total_price = total_price
    new_cart_item.item_id = item_id
    new_cart_item.order_id = order_id
    new_cart_item.product_name = product_name
    new_cart_item.product_picture = product_picture
    Cart.save(new_cart_item)
    return new_cart_item.pk


# This function updates the order subtotal for the customer order by taking in the action (add/remove) from the
# Javascript data passed in through the button on the page whether it is add to cart or the x to remove. It then takes
# the existing order record and the cart query to update both of those tables with the correct calculations. At the end
# of the function it returns the new subtotal variable.
def update_order_subtotal(action, existing_order, cart_query):
    new_subtotal = 0.00
    current_subtotal = existing_order.subtotal
    cart_item_price = cart_query.price
    if action == 'add':
        new_subtotal = current_subtotal + cart_item_price
        new_subtotal = round(new_subtotal, 2)
    if action == 'remove':
        new_subtotal = current_subtotal - cart_item_price
        new_subtotal = round(new_subtotal, 2)
        if new_subtotal < 0.01:
            new_subtotal = round(0.00, 2)
            new_subtotal = "{:.2f}".format(new_subtotal)
    return new_subtotal


# This function  determines the order delivery fee which is 5% of the total order. We pass in the action which is the
# data from the Javascript button pressed on the page (add/remove) the existing order record, and the cart query. We
# then perform calculations on the data whether we are adding or removing the item and then return the new delivery fee
# to the view in order to update the record in the database.
def update_order_delivery_fee(action, existing_order, cart_query):
    new_delivery_fee = decimal.Decimal(float(0.00))
    current_delivery_fee = existing_order.delivery_fee
    item_subtotal = cart_query.price
    delivery_fee_rate = decimal.Decimal(float(0.05))
    item_delivery_fee = item_subtotal * delivery_fee_rate
    if action == 'add':
        new_delivery_fee = current_delivery_fee + item_delivery_fee
        new_delivery_fee = round(new_delivery_fee, 2)
    if action == 'remove':
        new_delivery_fee = current_delivery_fee - item_delivery_fee
        new_delivery_fee = round(new_delivery_fee, 2)
        if new_delivery_fee < 0.01:
            new_delivery_fee = round(0.00, 2)
            new_delivery_fee = "{:.2f}".format(new_delivery_fee)
    return new_delivery_fee


# This function  determines the order tax which is 7.5% of the total order. We pass in the action which is the
# data from the Javascript button pressed on the page (add/remove) the existing order record, and the cart query. We
# then perform calculations on the data whether we are adding or removing the item and then return the new tax
# to the view in order to update the record in the database.
def update_order_tax(existing_order, action, cart_query):
    new_tax = decimal.Decimal(float(0.00))
    order_tax = existing_order.tax
    tax_rate = decimal.Decimal(float(0.075))
    item_subtotal = cart_query.price
    item_tax = item_subtotal * tax_rate
    if action == 'add':
        new_tax = order_tax + item_tax
        new_tax = round(new_tax, 2)
    if action == 'remove':
        new_tax = order_tax - item_tax
        new_tax = round(new_tax, 2)
        if new_tax < 0.01:
            new_tax = round(0.00, 2)
            new_tax = "{:.2f}".format(new_tax)
    return new_tax


# This function determines the order grand total which is a total calculation of the tax, delivery fee, and cart item
# price. We pass in the action which is the  data from the Javascript button pressed on the page (add/remove) the
# existing order record, and the cart query. We then perform calculations on the data whether we are adding or removing
# the item and then return the new tax to the view in order to update the record in the database.
def update_order_grand_total(existing_order, action, cart_query):
    new_grand_total = decimal.Decimal(float(0.00))
    current_order_grand_total = existing_order.grand_total
    tax_rate = decimal.Decimal(float(0.075))
    delivery_fee_rate = decimal.Decimal(float(0.05))
    item_subtotal = cart_query.price
    item_tax = item_subtotal * tax_rate
    item_delivery_fee = item_subtotal * delivery_fee_rate
    item_grand_total = item_subtotal + item_tax + item_delivery_fee
    if action == 'add':
        new_grand_total = current_order_grand_total + item_grand_total
        new_grand_total = round(new_grand_total, 2)
    if action == 'remove':
        new_grand_total = current_order_grand_total - item_grand_total
        new_grand_total = round(new_grand_total, 2)
        if new_grand_total < 0.01:
            new_grand_total = round(0.00, 2)
            new_grand_total = "{:.2f}".format(new_grand_total)
    return new_grand_total


# A function to get the delivery type for the user
def get_delivery_type(existing_order):
    delivery_type = existing_order.order_type_id
    print(delivery_type)
    return delivery_type


def get_locations():
    locations = Locations.objects.all()
    return locations

# A function to get the payment type for the user
def get_payment_type(existing_order):
    order_number = existing_order.pk
    payment = Payments.objects.get(order_number_id=order_number)
    payment_type_id = payment.payment_type_id
    payment_name = Payment_Types.objects.get(pk=payment_type_id)
    payment_name2 = payment_name.payment_method
    return payment_name2
