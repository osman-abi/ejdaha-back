from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import mixins
from .models import Customer, Courier, DeliveryPackages ,PredResults
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .serializers import  CustomerSerializer, CourierSerializer, DeliveryPackagesSerializer, PredSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import pickle
import pandas as pd 
from smtplib import SMTP
from rest_framework.response import Response


class CustomerAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def get(self, request):
        return self.list(request)
        
    def post(self, request):
        return self.create(request)



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



@csrf_exempt
def delivery_package(request):
    if request.method == 'GET':
        delivery_packages = DeliveryPackages.objects.all()
        serializer = DeliveryPackagesSerializer(delivery_packages, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DeliveryPackagesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            try:
                subject = "Delivery Module"
                message = "Sizin Sifarişiniz Yola Çıxdı.Təşəkkür edirik !"
                content = "Subject: {0}\n\n{1}".format(subject,message)

                myMailAdress = "muradaydin122@gmail.com"
                password = "Ma910910."

                sendTo = serializer.data.get('email')

                mail = SMTP("smtp.gmail.com", 587)
                mail.ehlo()
                mail.starttls()
                mail.login(myMailAdress,password)
                mail.sendmail(myMailAdress,sendTo,content.encode("utf-8"))
            except Exception as e:
                print("Error Handle\n {0}".format(e))
        
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def delivery_detail(request,id):
    delivery = DeliveryPackages.objects.get(id=id)
    serializer = DeliveryPackagesSerializer(delivery)
    return Response(serializer.data) 


class PostsView(generics.ListCreateAPIView):
    serializer_class = PredSerializer

    def get(self, request,*args,**kvargs):
        Recency = float(self.request.GET.get('Recency'))
        Frequency = float(self.request.GET.get('Frequency'))
        Monetary = float(self.request.GET.get('Monetary'))
        R = float(self.request.GET.get('R'))
        F = float(self.request.GET.get('F'))
        M = float(self.request.GET.get('M'))
        RFMGroup = float(self.request.GET.get('RFMGroup'))
        RFMScore = float(self.request.GET.get('RFMScore'))



        model = pd.read_pickle(r'C:\Users\Murad\Desktop\new_model.pickle')
 
        result = model.predict(
            [[Recency,Frequency,Monetary,R,F,M,RFMGroup,RFMScore]]
        )

        classification = result[0]
        serializer  = PredSerializer(data = self.request.GET)
        if serializer.is_valid():
            serializer.save()
            return Response(result[0])
        return Response(serializer.errors, status = 400)

