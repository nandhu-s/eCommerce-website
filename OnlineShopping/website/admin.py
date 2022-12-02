from django.contrib import admin
from .models import *

# Register your models here.
class Product_list(admin.ModelAdmin):
    list_display = ['name', 'category']

class Orders_list(admin.ModelAdmin):
    list_display = ['id', 'date', 'customer_id', 'product']

class Customer_list(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']

admin.site.register(Products, Product_list)
admin.site.register(Category)
admin.site.register(Customer, Customer_list)
admin.site.register(Order, Orders_list)