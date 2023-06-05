from django.contrib import admin
from .models import Product, Stock

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['id', 'address']
