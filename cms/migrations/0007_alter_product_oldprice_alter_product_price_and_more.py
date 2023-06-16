# Generated by Django 4.2.2 on 2023-06-16 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_product_availability_product_pack_alter_product_rrc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='oldprice',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Старая цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='rrc',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='РРЦ'),
        ),
    ]
