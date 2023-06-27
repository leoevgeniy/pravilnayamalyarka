from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Категория')
    description = models.TextField(null=True, blank=True, verbose_name="Описание Категории")
    # slug = models.SlugField(max_length=150, unique=True)

    # def get_absolute_url(self):
    #     return reverse('shop:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='subcategories',
                                 verbose_name='Категория')
    name = models.CharField(max_length=256, verbose_name="Подкатегория")
    description = models.TextField(null=True, blank=True, verbose_name='Описание Подкатегории')
    # slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering= ('name',)
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