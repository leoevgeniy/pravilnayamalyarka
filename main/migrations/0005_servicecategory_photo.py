# Generated by Django 4.2.2 on 2023-06-27 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_servicecategory_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecategory',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/service_category', verbose_name='Фото'),
        ),
    ]
