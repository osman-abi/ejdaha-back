from django.urls import path
from . import views
from .views import CustomerAPIView



urlpatterns = [
    path('account/register', views.UserCreate.as_view()),
    path('customer/<int:id>/', CustomerAPIView.as_view()),
    

]