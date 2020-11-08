from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import mixins
from .models import Customer
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import  CustomerSerializer



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




