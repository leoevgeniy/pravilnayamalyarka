# Generated by Django 4.2.2 on 2023-07-03 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_subcategory_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/service_category', verbose_name='Фото'),
        ),
    ]
