# Generated by Django 4.2.2 on 2023-08-31 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0056_promoslider_promoproduct_alter_product_unitofmeasure'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo5',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo6',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo7',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo8',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='product',
            name='youtubelink',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Состав'),
        ),
    ]