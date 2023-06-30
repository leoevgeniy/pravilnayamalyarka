# Generated by Django 4.2.2 on 2023-06-26 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_servicecategory_alter_category_options_and_more'),
        ('cms', '0015_service_service_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='workphoto',
            name='service_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.servicecategory', verbose_name='Категория'),
        ),
    ]