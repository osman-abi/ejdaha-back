from django.urls import path
from .views import CustomerAPIView
from . import views


urlpatterns = [
    path('customer/', CustomerAPIView.as_view()),
    path('customer/<int:id>', views.customer_detail),
    
    
    

]





