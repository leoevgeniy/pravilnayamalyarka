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
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


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
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    # def get_absolute_url(self):
    #     return reverse('shop:product_list_by_category', args=[self.slug])
