from django.contrib import admin
from apps.main.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', )


@admin.register(Brand)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', )


