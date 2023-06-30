# Generated by Django 4.2.2 on 2023-06-26 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_category_options_alter_subcategory_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Категория работ',
                'verbose_name_plural': 'Категории работ',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Категория товаров', 'verbose_name_plural': 'Категории товаров'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ('name',), 'verbose_name': 'Подкатегория товаров', 'verbose_name_plural': 'Подкатегории товаров'},
        ),
    ]