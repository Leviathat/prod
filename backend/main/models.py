import json
from django.db import models
from django.conf import settings
import random


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Брэнды'
        verbose_name = 'Брэнд'


class Product(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=25, choices=settings.PRODUCT_TYPE, blank=True, default=None)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.PositiveIntegerField(null=False, blank=False)
    sale_price = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.TimeField(auto_now_add=True)
    image = models.ImageField(verbose_name='Изображение', blank=True, upload_to="images/product/", null=True)
    sold = models.BooleanField(default=False)

    @property
    def product_info(self):
        return json.dumps({
                            'id': self.pk,
                            'name': self.name,
                            'type': self.type,
                            'brand': self.brand.name,
                            'price': self.price,
                            'sale': self.sale_price,
                           })

    def __str__(self):
        return f'{self.pk}/{self.name}/{self.type}/{self.price}/{self.sold}/{self.price}'


class Customer(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name="Имя покупателя")
    surname = models.CharField(max_length=255, null=True, verbose_name="Фамилия покупателя")
    number = models.CharField(max_length=255, null=True, verbose_name="Номер телефона покупателя")

    def __str__(self):
        return f'{self.surname} {self.name}, Номер: {self.number}'


class Cart(models.Model):
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True, unique=True)

    def __str__(self):
        return str(self.customer)

    @property
    def cart_total(self):
        total = sum([product.price for product in self.products.all()])
        return total

    @property
    def cart_items(self):
        orderitems = self.products.all()
        total = len(self.products.all())
        return total

    def save(self, *args, **kwargs):
        self.transaction_id = random.randint(100000, 999999)
        super(Cart, self).save(*args, **kwargs)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
