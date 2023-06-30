# Generated by Django 4.2.2 on 2023-06-26 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_alter_product_index_together_remove_product_slug'),
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
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Наименование')),
                ('service_pc', models.CharField(blank=True, max_length=20, null=True, verbose_name='Единица измерения')),
                ('service_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена за единицу')),
                ('service_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.servicecategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Вид работ',
                'verbose_name_plural': 'Виды работ',
            },
        ),
    ]