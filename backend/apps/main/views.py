from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse, HttpResponse
from apps.main.models import Product
from django.views.decorators.http import require_POST


def home(request):
    return redirect('home')


@require_POST
def make_order(request):



class ProductDetailView(DetailView):
    model = Product
    template_name = "product_article.html"
    context_object_name = 'product'


class ProductListView(ListView):
    paginate_by = 4
    model = Product
    template_name = "index.html"
    context_object_name = 'products'


class CheckoutView(TemplateView):
    template_name = "checkout.html"

