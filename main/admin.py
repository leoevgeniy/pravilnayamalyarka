from django.contrib import admin
from .models import Category, SubCategory, ServiceCategory


# Register your models here.

class SubCategoryAdm(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_display_links = ('name',)
    search_fields = ('name', 'category',)
    list_filter = ('category',)
    list_editable = ('category',)
    list_per_page = 10
    list_max_show_all = 100
    readonly_fields = ('id',)
    # поле класса комент
    # inlines = [Coment,]


admin.site.register(Category)
admin.site.register(SubCategory, SubCategoryAdm)


@admin.register(ServiceCategory)
class ServiceCategoryAdm(admin.ModelAdmin):
    list_display = ('name',)
