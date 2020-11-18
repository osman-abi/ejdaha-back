from django.urls import path
from .views import CustomerAPIView, CourierAPIView
from . import views


urlpatterns = [
    path('customer/', CustomerAPIView.as_view()),
    path('customer/<int:id>', views.customer_detail),
    path('courier/', CourierAPIView.as_view()),
    path('courier/<int:id>', views.courier_detail),
    
    
    ]





