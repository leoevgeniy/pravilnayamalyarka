# Generated by Django 4.2.2 on 2023-07-17 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0044_alter_packprice_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socials',
            name='social_network',
            field=models.CharField(choices=[('IG', 'Instagram'), ('FB', 'Facebook'), ('VK', 'VK'), ('TG', 'Telegram'), ('WA', 'Whatsapp'), ('VB', 'Viber'), ('YT', 'YouTube')], max_length=30, verbose_name='Соцсеть'),
        ),
    ]