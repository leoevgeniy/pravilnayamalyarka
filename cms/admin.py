from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdm(admin.ModelAdmin):
    list_display = ('name', 'vendor', 'price', 'oldprice', 'category', 'subcategory')
    list_editable = ('price', 'oldprice', 'category', 'subcategory',)

admin.site.register(Product, ProductAdm)
