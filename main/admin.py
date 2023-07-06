from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, SubCategory, ServiceCategory


# Register your models here.

class SubCategoryAdm(admin.ModelAdmin):
    list_display = ('id', 'get_img', 'name', 'category')
    list_display_links = ('name',)
    search_fields = ('name', 'category',)
    list_filter = ('category',)
    list_editable = ('category',)
    list_per_page = 10
    list_max_show_all = 100
    readonly_fields = ('id',)
    # поле класса комент
    # inlines = [Coment,]

    def get_img(self, obj):
        try:
            return mark_safe(f'<img src="{obj.photo.url}" width="80px"')
        except:
            return mark_safe(f'<img src="" width="80px"')

admin.site.register(SubCategory, SubCategoryAdm)


@admin.register(ServiceCategory)
class ServiceCategoryAdm(admin.ModelAdmin):
    list_display = ('name', 'get_img',)

    def get_img(self, obj):
        try:
            return mark_safe(f'<img src="{obj.photo.url}" width="80px"')
        except:
            return mark_safe(f'<img src="" width="80px"')


@admin.register(Category)
class CategoryAdm(admin.ModelAdmin):
    list_display = ('name', 'get_img',)

    def get_img(self, obj):
        try:
            return mark_safe(f'<img src="{obj.photo.url}" width="80px"')
        except:
            return mark_safe(f'<img src="" width="80px"')

