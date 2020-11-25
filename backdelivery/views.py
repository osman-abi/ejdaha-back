from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import mixins
from .models import Customer, Courier, DeliveryPackages
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import  CustomerSerializer, CourierSerializer, DeliveryPackagesSerializer
from rest_framework import status



class CustomerAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()



    def get(self, request):
        return self.list(request)
        



    def post(self, request):
        return self.create(request)

from rest_framework.response import Response

@api_view(['GET','DELETE'])
def customer_detail(request,id):
    customer = Customer.objects.get(id=id)
    
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data) 

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourierAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = CourierSerializer
    queryset = Courier.objects.all()


    def get(self, request):
        return self.list(request)
        



    def post(self, request):
        return self.create(request)



@api_view(['GET','PUT'])
def courier_detail(request,id):
    courier = Courier.objects.get(id=id)

    if request.method == 'GET':
        serializer = CourierSerializer(courier)
        return Response(serializer.data) 

    elif request.method == 'PUT':
        serializer = CourierSerializer(courier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeliveryAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = DeliveryPackagesSerializer
    queryset = DeliveryPackages.objects.all()


    def get(self, request):
        return self.list(request)
        



    def post(self, request):
        print('==================',self.serializer_class)
        return self.create(request)



@api_view(['GET'])
def delivery_detail(request,id):
    delivery = DeliveryPackages.objects.get(id=id)
    serializer = DeliveryPackagesSerializer(delivery)
    return Response(serializer.data) 
