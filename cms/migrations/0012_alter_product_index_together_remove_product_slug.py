# Generated by Django 4.2.2 on 2023-06-20 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_alter_product_options_product_slug_and_more'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='product',
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]