from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='Shopindex'),
    path('about/', views.about, name='About'),
    path('contact/', views.contact, name='Contact'),
    path('search/', views.search, name='Search'),
    path('productView/', views.productView, name='ProductView'),
    path('product/<int:id>', views.Allproduct, name='Product'),
    path('tracker/', views.tracker, name='Tracking'),
    path('checkout/', views.checkout, name='checkOut'),
    path('cartView/', views.cartView, name='cartView'),
    path('category/', views.categorywiseproductView, name='Category'),
]
