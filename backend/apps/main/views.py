from django.views.generic import TemplateView, ListView, DetailView
from django.http.response import JsonResponse
from rest_framework import status
from apps.main.models import *
from rest_framework.views import APIView
from apps.main.serializers import *
import json
from apps.main.tasks.tg_notion import tg_msg
from django.conf import settings
from apps.main.renderers import CartJSONRenderer


class RegisterView(TemplateView):
    template_name = "register.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_article.html"
    context_object_name = 'product'


class ProductListView(ListView):
    paginate_by = 4
    model = Product
    template_name = "index.html"
    context_object_name = 'products'
    ordering = ['-id']


class CheckoutView(TemplateView):
    template_name = "checkout.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['cities'] = settings.CITY
        return context


class TestAPIView(APIView):

    authentication_classes = ()
    renderer_classes = (CartJSONRenderer,)

    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))
        order = {
            'cart': body.get('cart', None),
            'email': body.get('email', None),
            'phone': body.get('phone', None),
            'fio': body.get('fio', None),
            'city': body.get('city', None),
            'street': body.get('street', None),
            'house': body.get('house', None),
            'summary': body.get('summary', None)
        }
        print(order)
        res = OrderSerializer(data=order)
        res.is_valid(raise_exception=True)
        res.save()
        tg_msg(order)
        return JsonResponse(data={'success': 'true'}, status=status.HTTP_201_CREATED)
