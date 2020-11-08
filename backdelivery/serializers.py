from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','ad','soyad','phone_number','email')


