# Generated by Django 4.2.2 on 2023-06-23 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_alter_product_index_together_remove_product_slug'),
        ('crm', '0009_alter_orderitems_order_alter_orderitems_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='image',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cms.product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='qty',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Кол-во'),
        ),
    ]