from django.db import models
from django.contrib.sites.models import Site
from meta.models import ModelMeta


# Create your models here.
class Page(models.Model, ModelMeta):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)

    def get_meta_title(self):
        return self.title

    def get_meta_description(self):
        return self.description

    def get_meta_keywords(self):
        return self.keywords

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Категория')
    description = models.TextField(null=True, blank=True, verbose_name="Описание Категории")
    photo = models.ImageField(upload_to="images/category", verbose_name="Фото", null=True, blank=True)

    # slug = models.SlugField(max_length=150, unique=True)

    # def get_absolute_url(self):
    #     return reverse('shop:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name

    _metadata = {
        'title': name,
        'description': description,
        'image': 'photo_url',
    }

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='subcategories',
                                 verbose_name='Категория')
    name = models.CharField(max_length=256, verbose_name="Подкатегория")
    description = models.TextField(null=True, blank=True, verbose_name='Описание Подкатегории')
    photo = models.ImageField(upload_to="images/subcategory", verbose_name="Фото", null=True, blank=True)

    # slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    class Meta:
        ordering = ('name',)
        verbose_name = 'Подкатегория товаров'
        verbose_name_plural = 'Подкатегории товаров'

    # def get_absolute_url(self):
    #     return reverse('shop:product_list_by_category', args=[self.slug])


class ServiceCategory(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, verbose_name='Наименование')
    photo = models.ImageField(upload_to="images/service_category", verbose_name="Фото", null=True, blank=True)

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория работ'
        verbose_name_plural = 'Категории работ'
