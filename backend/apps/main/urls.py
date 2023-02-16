from django.urls import path, include
from apps.main.views import *

urlpatterns = [
    path('', home, name='main'),
    path('home/', ProductListView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order/', make_order, name='make-order')
]
