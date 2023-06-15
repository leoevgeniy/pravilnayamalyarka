from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from main.models import Category, SubCategory

# Create your models here.

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categoryproducts', verbose_name='Категория')
    subcategory = ChainedForeignKey(
        SubCategory,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    name = models.CharField(max_length=256, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    vendor = models.CharField(max_length=256, verbose_name='Производитель')
    weight = models.CharField(max_length=50, verbose_name='Вес')
    composition = models.CharField(max_length=256, verbose_name='Состав')
    comments = models.TextField(verbose_name='Примечание')
    agelimit = models.DateField(max_length=256, verbose_name='Срок годности')
    consimption = models.TextField(max_length=256, verbose_name='Расход')
    photo = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Создано")
    time_update = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Обновлено")
    price = models.FloatField(verbose_name='Цена')
    oldprice = models.FloatField(verbose_name='Старая цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


