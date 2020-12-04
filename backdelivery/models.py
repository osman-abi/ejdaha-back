from django.db import models


class Customer(models.Model):
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=100)
    musterinin_sifarisi = models.CharField(max_length=50)
    location = models.CharField(max_length=250)
    total = models.CharField(max_length=50)
    time = models.CharField(max_length=10)
    
    def __str__(self):
        return self.ad

class Courier(models.Model):
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True)
    is_busy = models.BooleanField(default=False)

    def __str__(self):
        return self.ad

class DeliveryPackages(models.Model):
    musterinin_adi = models.CharField(max_length=50)
    musterinin_soyadi = models.CharField(max_length=50)
    musterinin_sifarisi = models.CharField(max_length=50)
    musterinin_nomresi = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=100)
    kuryerin_adi = models.CharField(max_length=50)
    kuryerin_soyadi = models.CharField(max_length=50)
    kuryerin_nomresi = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=250)
    total = models.CharField(max_length=50)

    def __str__(self):
        return self.musterinin_sifarisi




class PredResults(models.Model):
    Recency = models.FloatField()
    Frequency = models.FloatField()
    Monetary = models.FloatField()
    R = models.FloatField()
    F = models.FloatField()
    M = models.FloatField()
    RFMGroup = models.FloatField()
    RFMScore = models.FloatField()









