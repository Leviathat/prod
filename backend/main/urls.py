from django.urls import path, include
from main.views import *

urlpatterns = [
    path('home/', ProductListView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
