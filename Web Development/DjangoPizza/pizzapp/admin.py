from django.contrib import admin
from .models import Customer
from .models import Cart
from .models import Order
from .models import Product
from .models import Locations
from .models import ProductTypes
from .models import Order_Type


# Register your models here.
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Locations)
admin.site.register(ProductTypes)
admin.site.register(Order_Type)