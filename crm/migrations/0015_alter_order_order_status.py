# Generated by Django 4.2.2 on 2023-06-26 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0014_alter_commentcrm_comment_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.statuscrm', verbose_name='Статус'),
        ),
    ]
