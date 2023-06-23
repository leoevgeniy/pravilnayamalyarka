# Generated by Django 4.2.2 on 2023-06-23 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_alter_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='crm.statuscrm', verbose_name='Статус'),
        ),
    ]
