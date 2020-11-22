from django.contrib import admin
from .models import (Customer, Courier, DeliveryPackages)

admin.site.register(Customer)
admin.site.register(Courier)
admin.site.register(DeliveryPackages)
# Register your models here.
