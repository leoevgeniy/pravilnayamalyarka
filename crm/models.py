from django.contrib.auth.models import User
from django.db import models

from cms.models import Product


class StatusCrm(models.Model):
    status_name = models.CharField(max_length=200, verbose_name='Статус')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    order_type = models.CharField(max_length=200, verbose_name='Тип Заказа', null=True, blank=True)
    order_status = models.ForeignKey(StatusCrm, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Статус')

    @property
    def number_of_items(self):
        return self.orderitems.count()

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, verbose_name='Товар')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='orderitems')
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Наименование')
    qty = models.IntegerField(null=True, blank=True, default=0, verbose_name='Кол-во')
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Цена')
    image = models.CharField(max_length=200, null=True, blank=True, verbose_name='Изображение')
    vendor_code = models.CharField(max_length=256, verbose_name='Код от производителя', null=True, blank=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='Стоимость')

    def get_cost(self):
        return self.price * self.qty

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Заказанный товар'
        verbose_name_plural = 'Заказанные товары'


def logged_user(request):
    current_user = request.user
    return current_user


class CommentCrm(models.Model):
    comment_owner = models.ForeignKey(User, editable=False, on_delete=models.DO_NOTHING,
                                      verbose_name='Оставил комментарий', null=True, blank=True)
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Дата создания комментария')

    def __str__(self):
        return self.comment_text


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
