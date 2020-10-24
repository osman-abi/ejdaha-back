from django.db import models


class Customer(models.Model):
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=100)








