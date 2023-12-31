# Generated by Django 4.2.2 on 2023-06-16 10:25

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('cms', '0009_alter_product_oldprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categoryproducts', to='main.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='category', chained_model_field='category', null=True, on_delete=django.db.models.deletion.CASCADE, to='main.subcategory'),
        ),
    ]
