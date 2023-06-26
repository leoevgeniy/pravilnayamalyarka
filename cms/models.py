from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from main.models import Category, SubCategory, ServiceCategory


# Create your models here.

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categoryproducts', verbose_name='Категория', null=True, blank=True)
    subcategory = ChainedForeignKey(
        SubCategory,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=256, verbose_name='Наименование', null=True, blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    vendor_code = models.CharField(max_length=256, verbose_name='Код от производителя', null=True, blank=True)
    vendor = models.CharField(max_length=256, verbose_name='Производитель', null=True, blank=True)
    weight = models.CharField(max_length=50, verbose_name='Вес', null=True, blank=True)
    composition = models.CharField(max_length=256, verbose_name='Состав', null=True, blank=True)
    comments = models.TextField(verbose_name='Примечание', null=True, blank=True)
    agelimit = models.DateField(max_length=256, verbose_name='Срок годности', null=True, blank=True)
    consimption = models.TextField(max_length=256, verbose_name='Расход', null=True, blank=True)
    photo = models.ImageField(upload_to="images/", verbose_name="Фото", null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Создано", null=True, blank=True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Обновлено", null=True, blank=True)
    price = models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Цена', null=True, blank=True)
    rrc = models.DecimalField(decimal_places=0, max_digits=10, verbose_name='РРЦ', null=True, blank=True)
    availability = models.CharField(max_length=256, verbose_name='Наличие', null=True, blank=True)
    pack = models.ImageField()
    # slug = models.SlugField(max_length=200, db_index=True)
    oldprice = models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Старая цена', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        # index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    # def get_absolute_url(self):
    #     return reverse('product_detail', args=[self.id, self.slug])

class WorkPhoto(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, verbose_name='Наименование')
    photo = models.ImageField(upload_to="images/donework", null=True, blank=True, verbose_name="Фото Наших работ")

    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name = 'Фото работ'
        verbose_name_plural = 'Фото работ'





class Service(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, verbose_name='Наименование')
    service_pc = models.CharField(max_length=20, blank=True, null=True, verbose_name='Единица измерения')
    service_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за единицу')
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, verbose_name="Категория")
    service_code = models.CharField(max_length=256, verbose_name='Код вида работ', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид работ'
        verbose_name_plural = 'Виды работ'