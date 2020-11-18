from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import mixins
from .models import Customer, Courier
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import  CustomerSerializer, CourierSerializer



class CustomerAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()



    def get(self, request):
        return self.list(request)
        



    def post(self, request):
        return self.create(request)

from rest_framework.response import Response

@api_view(['GET'])
def customer_detail(request,id):
    customer = Customer.objects.get(id=id)
    serializer = CustomerSerializer(customer)
    return Response(serializer.data) 



class CourierAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = CourierSerializer
    queryset = Courier.objects.all()


    def get(self, request):
        return self.list(request)
        



    def post(self, request):
        return self.create(request)



@api_view(['GET'])
def courier_detail(request,id):
    courier = Courier.objects.get(id=id)
    serializer = CourierSerializer(courier)
    return Response(serializer.data) 