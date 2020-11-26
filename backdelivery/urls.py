from django.urls import path
from .views import CustomerAPIView, CourierAPIView, PostsView
from . import views


urlpatterns = [
    path('customer/', CustomerAPIView.as_view()),
    path('customer/<int:id>/', views.customer_detail),
    path('courier/', CourierAPIView.as_view()),
    path('courier/<int:id>/', views.courier_detail),
    path('delivery/', views.delivery_package),
    path('delivery/<int:id>/', views.delivery_detail),
    path('posts/',PostsView.as_view(),name = 'posts_view')
    
    
    ]





