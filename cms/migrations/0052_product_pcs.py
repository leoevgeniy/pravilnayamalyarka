# Generated by Django 4.2.2 on 2023-07-31 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0051_alter_ourphoto_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pcs',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Единица измерения'),
        ),
    ]
