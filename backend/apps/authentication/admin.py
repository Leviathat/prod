from django.contrib import admin
from apps.authentication.models import User


@admin.register(User)
class UserUser(admin.ModelAdmin):
    list_display = ('fio', 'phone_number', 'email', )

