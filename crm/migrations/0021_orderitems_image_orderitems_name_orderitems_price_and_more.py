# Generated by Django 4.2.2 on 2023-07-31 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0020_remove_orderitems_image_remove_orderitems_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='image',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='orderitems',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='orderitems',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='orderitems',
            name='vendor_code',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Код от производителя'),
        ),
    ]
