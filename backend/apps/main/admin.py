from django.contrib import admin
from apps.main.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', )


@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('cart', 'address', 'customer')


@admin.register(Address)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('city', 'street', 'house')
