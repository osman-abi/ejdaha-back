from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer, Courier, DeliveryPackages



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','ad','soyad','phone_number','email','musterinin_sifarisi','location','total')

class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = ('ad', 'soyad', 'phone_number', 'is_busy')


class DeliveryPackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPackages
        fields = '__all__'