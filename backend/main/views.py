from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from main.models import Product


class HomeView(TemplateView):
    template_name = "index.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_article.html"
    context_object_name = 'product'


class ProductListView(ListView):
    paginate_by = 2
    model = Product
    template_name = "index.html"
    context_object_name = 'products'



