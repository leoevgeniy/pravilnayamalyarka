from django.db import models


# Create your models here.

class TeleSettings(models.Model):
    token = models.CharField(max_length=200, verbose_name='Токен')
    chan_id = models.CharField(max_length=200, verbose_name='Чат ID')
    message = models.TextField(verbose_name='Текст сообщения')

    def __str__(self):
        return self.chan_id

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
