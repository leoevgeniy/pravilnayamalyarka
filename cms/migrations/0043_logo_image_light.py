# Generated by Django 4.2.2 on 2023-07-14 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0042_remove_promoslider_vendor_code_list_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='logo',
            name='image_light',
            field=models.FileField(blank=True, null=True, upload_to='images/logo', verbose_name='Логотип светлый'),
        ),
    ]
