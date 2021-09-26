from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class ProductTypes(models.Model):
    product_type_description = models.CharField(max_length=25)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    item_type_id = models.ForeignKey(ProductTypes, on_delete=models.CASCADE, db_column="item_type_id")


class Order_Type(models.Model):
    type = models.CharField(max_length=50)


class Locations(models.Model):
    location_name = models.CharField(max_length=50)
    location_address = models.CharField(max_length=50)
    location_city = models.CharField(max_length=50)
    location_state = models.CharField(max_length=25)
    location_zip = models.IntegerField()
    location_image = models.TextField(null=True)


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    delivery_type = models.IntegerField(null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=25, null=True)
    zip_code = models.IntegerField(null=True)
    email = models.CharField(max_length=50, null=True)
    phone_number = models.BigIntegerField(null=True)
    visitor_id = models.BigIntegerField(null=True)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    order_type = models.ForeignKey(Order_Type, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE, null=True, related_name="related_location")
    subtotal = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    delivery_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    tax = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    grand_total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    order_completed = models.BooleanField(null=True)


class Cart(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name="related_order")
    item = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="related_item")
    quantity = models.DecimalField(max_digits=4, decimal_places=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_name = models.CharField(max_length=100, null=True)
    product_picture = models.TextField(default='Does Not Exist')


class Careers(models.Model):
    position = models.CharField(max_length=50, null=True)
    from_email = models.CharField(max_length=50, null=True)
    resume = models.CharField(max_length=3000, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone_number = models.BigIntegerField(null=True)


class Payment_Types(models.Model):
    payment_method = models.CharField(max_length=20, null=True)


class Payments(models.Model):
    customer_number = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, related_name="related_customer")
    order_number = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name="order_number")
    payment_type = models.ForeignKey(Payment_Types, on_delete=models.CASCADE, null=True, related_name="related_payment_type")
    payment_total = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)


class Credit_Card_Types(models.Model):
    card_type = models.CharField(max_length=50, null=True)


class Payment_Details(models.Model):
    billing_full_name = models.CharField(max_length=50, null=True)
    billing_email = models.CharField(max_length=50, null=True)
    billing_address = models.CharField(max_length=100, null=True)
    billing_city = models.CharField(max_length=50, null=True)
    billing_state = models.CharField(max_length=25, null=True)
    billing_zip = models.IntegerField(null=True)
    payment = models.ForeignKey(Payments, on_delete=models.CASCADE, null=True, related_name="related_payment")
    customer_name = models.CharField(max_length=100, null=True)
    billing_name = models.CharField(max_length=100, null=True)
    credit_card_number = models.BigIntegerField(null=True)
    expiration_month = models.CharField(max_length=50, null=True)
    expiration_year = models.CharField(max_length=50, null=True)
    security_code = models.IntegerField(null=True)
    type = models.ForeignKey(Credit_Card_Types, on_delete=models.CASCADE, null=True, related_name="related_card_type")


class Promo_Code_Payment(models.Model):
    promo_code_used = models.IntegerField(null=True)
    payment = models.ForeignKey(Payments, on_delete=models.CASCADE, null=True, related_name="promo_payment")


class Cash_Payment(models.Model):
    payment = models.ForeignKey(Payments, on_delete=models.CASCADE, null=True, related_name="cash_payment")