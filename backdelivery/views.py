from django.shortcuts import render
from rest_framework import generics
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )