from django.urls import path
from apps.main.views import *
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='home'), name='main'),
    path('home/', ProductListView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order/', TestAPIView.as_view(), name='make-order'),
    path('register/', RegisterView.as_view(), name='register')
]
