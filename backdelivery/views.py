from django.shortcuts import render
from rest_framework import generics
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import mixins
from .serializer import CustomerSerializer
from .models import Customer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class CustomerAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)

        else:
            return self.list(request)



    def post(self, request):
        return self.create(request)



    def put(self, request, id=None):
        return self.update(request, id)


    def delete(self, request, id):
        return self.destroy(request, id)

