from django.contrib import admin
from .models import (Customer, Courier, DeliveryPackages,PredResults)

admin.site.register(Customer)
admin.site.register(Courier)
admin.site.register(DeliveryPackages)
admin.site.register(PredResults)
# Register your models here.
