from django.contrib import admin
from django.utils.safestring import mark_safe
# from import_export.admin import ImportExportActionModelAdmin
from import_export import resources



from .models import Product, WorkPhoto


# Register your models here.
class ProductResources(resources.ModelResource):

    class Meta:
        model = Product


# class ProductAdm(ImportExportActionModelAdmin):
#     resource_class = ProductResources
#     list_display = ('vendor_code', 'get_img', 'name', 'vendor', 'price', 'oldprice', 'category', 'subcategory')
#     list_editable = ('price', 'oldprice', 'category', 'subcategory',)
#     list_filter = ('vendor', 'category', 'subcategory',)
#     list_per_page = 50
#     list_max_show_all = 100
#
#     def get_img(self, obj):
#         try:
#             return mark_safe(f'<img src="{obj.photo.url}" width="80px"')
#         except:
#             return mark_safe(f'<img src="" width="80px"')
class ProductAdm(admin.ModelAdmin):
    list_display = ('get_img', 'name', 'vendor', 'price', 'oldprice', 'category', 'subcategory')
    list_editable = ('price', 'oldprice', 'category', 'subcategory',)
    list_filter = ('vendor', 'category', 'subcategory',)
    list_per_page = 20
    list_max_show_all = 100

    def get_img(self, obj):
        try:
            return mark_safe(f'<img src="{obj.photo.url}" width="80px"')
        except:
            return mark_safe(f'<img src="" width="80px"')


class WorkPhotoAdm(admin.ModelAdmin):
    list_display = ('get_img', 'name',)
    list_per_page = 20
    list_max_show_all = 100

    def get_img(self, obj):
        try:
            return mark_safe(f'<img src="{obj.photo.url}" width="80px"')
        except:
            return mark_safe(f'<img src="" width="80px"')


admin.site.register(Product, ProductAdm)
admin.site.register(WorkPhoto, WorkPhotoAdm)
