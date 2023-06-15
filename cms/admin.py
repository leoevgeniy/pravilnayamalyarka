from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product

# Register your models here.

class ProductAdm(admin.ModelAdmin):
    list_display = ('get_img', 'name', 'vendor', 'price', 'oldprice', 'category', 'subcategory')
    list_editable = ('price', 'oldprice', 'category', 'subcategory',)
    list_filter = ('vendor', 'category', 'subcategory',)
    list_per_page = 20
    list_max_show_all = 100

    def get_img(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" width="80px"')

admin.site.register(Product, ProductAdm)
