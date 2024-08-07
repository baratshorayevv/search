# online_shop/urls.py
from django.urls import path
from .views import product_detail, product_search

urlpatterns = [
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('search/', product_search, name='product_search'),
]
