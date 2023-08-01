from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from main.models import Category, SubCategory, ServiceCategory


class Vendor(models.Model):
    name = models.CharField(max_length=256, verbose_name='Наименование', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


# Create your models here.
class PromoSlider(models.Model):
    name = models.CharField(max_length=256, verbose_name='Наименование', null=True, blank=True)
    description = models.CharField(max_length=256, verbose_name='Описание', null=True, blank=True)
    photo = models.ImageField(upload_to="images/slider", verbose_name="Фото", null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name='Производитель', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='promos',
                                       verbose_name='Категория', null=True, blank=True)
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
    start_date = models.DateField(verbose_name='Дата начала акции', null=True, blank=True)
    expiration_date = models.DateField(verbose_name='Дата окончания акции', null=True, blank=True)

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    # def __str__(self):
    #     return self.name

    class Meta:
        ordering = ('expiration_date',)
        # index_together = (('id', 'slug'),)
        verbose_name = 'Промо акция'
        verbose_name_plural = 'Промо акции'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categoryproducts',
                                 verbose_name='Категория', null=True, blank=True)
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
    pcs = 'шт'
    liters = 'л'
    pack = 'упаковка'
    unit = [
        (pcs, 'шт'),
        (liters, 'л'),
        (pack, 'упаковка'),
    ]
    unitofmeasure = models.CharField(max_length=30, choices=unit, verbose_name='Единица измерения', null=True, blank=True)
    name = models.CharField(max_length=256, verbose_name='Наименование', null=True, blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    vendor_code = models.IntegerField(verbose_name='Код от производителя', null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name='Производитель', null=True, blank=True)
    composition = models.CharField(max_length=256, verbose_name='Состав', null=True, blank=True)
    comments = models.TextField(verbose_name='Примечание', null=True, blank=True)
    agelimit = models.DateField(max_length=256, verbose_name='Срок годности', null=True, blank=True)
    consimption = models.TextField(max_length=256, verbose_name='Расход', null=True, blank=True)
    photo = models.ImageField(upload_to="images/", verbose_name="Фото", null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Создано", null=True, blank=True)
    time_update = models.DateTimeField(auto_now=True, verbose_name="Обновлено", null=True, blank=True)
    rrc = models.DecimalField(decimal_places=0, max_digits=10, verbose_name='РРЦ', null=True, blank=True)
    availability = models.CharField(max_length=256, verbose_name='Наличие', null=True, blank=True)
    pack = models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Кол-ва в Упаковке', null=True, blank=True)

    # price = models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Цена', null=True, blank=True)

    # slug = models.SlugField(max_length=200, db_index=True)
    @property
    def firstprice(self):
        packprice = self.packprices.all()[0].price
        return packprice


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


class Packprice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, verbose_name='Товар',
                                related_name='packprices')
    weight = models.CharField(max_length=256, verbose_name='Объем', null=True, blank=True)
    # pack = models.ImageField(upload_to="images/pack", verbose_name='Упаковка', null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена', null=True, blank=True)
    oldprice = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Старая цена', null=True, blank=True)

    @property
    def firstprice(self):
        packprice = self.objects.all()[0].price
        return packprice

    def __str__(self):
        return self.weight + '/ Цена: ' + str(self.price) + '/Старая цена: ' + str(self.oldprice)

    class Meta:
        ordering = ('price',)
        # index_together = (('id', 'slug'),)
        verbose_name = 'Вес'
        verbose_name_plural = 'Веса'


class WorkPhoto(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, verbose_name='Наименование')
    photo = models.ImageField(upload_to="images/donework", null=True, blank=True, verbose_name="Фото Наших работ")
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, verbose_name="Категория", null=True,
                                         blank=True)

    # def __str__(self):
    #     return self.name
    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    class Meta:
        verbose_name = 'Фото работ'
        verbose_name_plural = 'Фото работ'


class OurPhoto(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, verbose_name='Наименование')
    photo = models.ImageField(upload_to="images/ourteam", null=True, blank=True, verbose_name="Наши фото")

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    class Meta:
        verbose_name = 'Наши фото'
        verbose_name_plural = 'Наши фото'


class Services_files(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, verbose_name='Наименование')
    file = models.FileField(upload_to="images/pricelists", null=True, blank=True, verbose_name="Файл с прайс листом")
    inuse = models.BooleanField(null=True, blank=True, verbose_name='Использовать на сайте')

    def save(self, *args, **kwargs):
        if self.inuse:
            try:
                temp = Services_files.objects.get(inuse=True)
                if self != temp:
                    temp.inuse = False
                    temp.save()
            except Services_files.DoesNotExist:
                pass
        super(Services_files, self).save(*args, **kwargs)



    @property
    def file_url(self):
        if self.file and hasattr(self.file, 'url'):
            return self.file.url
    class Meta:
        verbose_name = 'Прайс лист'
        verbose_name_plural = 'Прайс листы'


class Services_calculation_cost(models.Model):
    house = models.CharField(max_length=256, blank=True, null=True, verbose_name='Дом')
    apartment = models.CharField(max_length=256, blank=True, null=True, verbose_name='Квартира')
    plant = models.CharField(max_length=256, blank=True, null=True, verbose_name='Промышленное помещение')
    inuse = models.BooleanField(null=True, blank=True, verbose_name='Использовать на сайте')

    def save(self, *args, **kwargs):
        if self.inuse:
            try:
                temp = Services_calculation_cost.objects.get(inuse=True)
                if self != temp:
                    temp.inuse = False
                    temp.save()
            except Services_calculation_cost.DoesNotExist:
                pass
        super(Services_calculation_cost, self).save(*args, **kwargs)



    class Meta:
        verbose_name = 'Стоимость работ для калькулятора'
        verbose_name_plural = 'Стоимости работ для калькулятора'


class Service(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, verbose_name='Наименование')
    photo = models.ImageField(upload_to="images/donework", null=True, blank=True, verbose_name="Фото Вида работ")
    service_pc = models.CharField(max_length=20, blank=True, null=True, verbose_name='Единица измерения')
    service_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за единицу')
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, verbose_name="Категория")
    service_code = models.CharField(max_length=256, verbose_name='Код вида работ', null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url


    class Meta:
        verbose_name = 'Вид работ'
        verbose_name_plural = 'Виды работ'


class Introduction(models.Model):
    text = models.TextField(verbose_name='Вводный текст о компании', null=True, blank=True)
    inuse = models.BooleanField(null=True, blank=True, verbose_name='Использовать на сайте')

    def save(self, *args, **kwargs):
        if self.inuse:
            try:
                temp = Introduction.objects.get(inuse=True)
                if self != temp:
                    temp.inuse = False
                    temp.save()
            except Introduction.DoesNotExist:
                pass
        super(Introduction, self).save(*args, **kwargs)

    class Meta:
            verbose_name = 'О компании'
            verbose_name_plural = 'О компании'


class Logo(models.Model):
    image = models.FileField(upload_to="images/logo", null=True, blank=True, verbose_name="Логотип")
    image_light = models.FileField(upload_to="images/logo", null=True, blank=True, verbose_name="Логотип светлый")
    inuse = models.BooleanField(null=True, blank=True, verbose_name='Использовать на сайте')

    def save(self, *args, **kwargs):
        if self.inuse:
            try:
                temp = Logo.objects.get(inuse=True)
                if self != temp:
                    temp.inuse = False
                    temp.save()
            except Logo.DoesNotExist:
                pass
        super(Logo, self).save(*args, **kwargs)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    @property
    def image_light_url(self):
        if self.image_light and hasattr(self.image_light, 'url'):
            return self.image_light.url

    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотипы'


class Socials(models.Model):
    Instagram = 'IG'
    Facebook = 'FB'
    VK = 'VK'
    Telegram = 'TG'
    Whatsapp = 'WA'
    Viber = 'VB'
    YouTube = 'YT'
    social_network_choices = [
        (Instagram, 'Instagram'),
        (Facebook, 'Facebook'),
        (VK, 'VK'),
        (Telegram, 'Telegram'),
        (Whatsapp, 'Whatsapp'),
        (Viber, 'Viber'),
        (YouTube, 'YouTube'),
        ]
    social_network = models.CharField(max_length=30, choices=social_network_choices, verbose_name='Соцсеть')
    link = models.CharField(max_length=250, verbose_name='Ссылка на социальную сеть')
    image = models.FileField(upload_to="images/socials", null=True, blank=True, verbose_name="Логотип Соцсети")

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self):
        return self.social_network

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

class Contacts(models.Model):
    phone1 = models.CharField(max_length=250, null=True, blank=True, verbose_name='Номер телефона для контактов')
    phone2 = models.CharField(max_length=250, null=True, blank=True, verbose_name='Номер телефона для контактов')
    phone3 = models.CharField(max_length=250, null=True, blank=True, verbose_name='Номер телефона для контактов')
    address1 = models.CharField(max_length=250, null=True, blank=True, verbose_name='Адрес')
    address2 = models.CharField(max_length=250, null=True, blank=True, verbose_name='Адрес')
    address3 = models.CharField(max_length=250, null=True, blank=True, verbose_name='Адрес')
    email1 = models.EmailField(null=True, blank=True, verbose_name='E-mail')
    email2 = models.EmailField(null=True, blank=True, verbose_name='E-mail')
    email3 = models.EmailField(null=True, blank=True, verbose_name='E-mail')

    class Meta:
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Контактные данные'