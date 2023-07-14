from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from django.utils.safestring import mark_safe
# from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from .models import Product, WorkPhoto, Service, PromoSlider, Vendor, Packprice, Introduction, Logo, Socials, Contacts
from cms.forms import UploadFileForm


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
def upload_products(request):
    form = UploadFileForm

    return render(request, "admin/upload_form.html", {'form': form})


def upload_services(request):
    form = UploadFileForm

    return render(request, "admin/upload_services_form.html", {'form': form})


class PackPriceAdm(admin.TabularInline):
    # list_display = ('weight', 'price', 'oldprice', )
    model = Packprice
    extra = 0
    fields = ('weight', 'price', 'oldprice',)
    # readonly_fields = ('comment_dt', 'comment_owner',)


class ProductAdm(admin.ModelAdmin):
    # change_list_template = 'admin/cms/product/change_list.html'
    list_display = ('get_img', 'name', 'vendor', 'category', 'subcategory')
    list_editable = ('category', 'subcategory',)
    list_filter = ('vendor', 'category', 'subcategory',)
    list_per_page = 20
    list_max_show_all = 100

    inlines = [
        PackPriceAdm,


    ]
    def get_img(self, obj):
        try:
            return mark_safe(f'<img src="{obj.photo.url}" width="80px"')
        except:
            return mark_safe(f'<img src="" width="80px"')

    def get_urls(self):
        urls = super().get_urls()
        new_url = [path('upload_products/', upload_products, name='upload_products')]
        return new_url + urls


class WorkPhotoAdm(admin.ModelAdmin):
    list_display = ('get_img', 'name', 'service_category',)
    list_editable = ('service_category',)
    list_per_page = 20
    list_max_show_all = 100

    def get_img(self, obj):
        try:
            return mark_safe(f'<img src="{obj.photo.url}" width="80px"')
        except:
            return mark_safe(f'<img src="" width="80px"')


admin.site.register(Product, ProductAdm)
admin.site.register(WorkPhoto, WorkPhotoAdm)


@admin.register(Service)
class ServicesAdm(admin.ModelAdmin):
    list_display = ('name', 'service_category', 'service_pc', 'service_price',)
    list_per_page = 20
    list_max_show_all = 100
    list_filter = ('service_category',)
    list_editable = ('service_price', 'service_category',)

    def get_urls(self):
        urls = super().get_urls()
        new_url = [path('upload_services/', upload_services, name='upload_services')]
        return new_url + urls


@admin.register(PromoSlider)
class PromoSliderAdm(admin.ModelAdmin):
    list_display = ('get_img', 'name', 'vendor', 'start_date', 'expiration_date')
    list_per_page = 20
    list_max_show_all = 100
    list_filter = ('vendor',)
    list_editable = ('name', 'start_date', 'expiration_date',)

    def get_img(self, obj):
        try:
            return mark_safe(f'<img src="{obj.photo.url}" width="80px"')
        except:
            return mark_safe(f'<img src="" width="80px"')

@admin.register(Vendor)
class VendorAdm(admin.ModelAdmin):
    list_display = ('name', )
    list_per_page = 20
    list_max_show_all = 100
    # list_editable = ('name', )

@admin.register(Logo)
class LogoAdm(admin.ModelAdmin):
    # fields = ('get_img', )
    list_display = ('get_img', 'inuse',)

    def get_img(self, obj):
        try:
            return mark_safe(f'<img src="{obj.image.url}" width="80px"')
        except:
            return mark_safe(f'<img src="" width="80px"')

@admin.register(Introduction)
class IntroductionAdm(admin.ModelAdmin):
    # fields = ('get_img', )
    list_display = ('text', 'inuse',)

    def get_img(self, obj):
        try:
            return mark_safe(f'<img src="{obj.image.url}" width="80px"')
        except:
            return mark_safe(f'<img src="" width="80px"')

@admin.register(Socials)
class IntroductionAdm(admin.ModelAdmin):
    # fields = ('get_img', )
    list_display = ('social_network', 'link',)

@admin.register(Contacts)
class ContactsAdm(admin.ModelAdmin):
    # fields = ('get_img', )
    list_display = ('phone1', 'address1',)


