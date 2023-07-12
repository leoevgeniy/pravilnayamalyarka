# Generated by Django 4.2.2 on 2023-07-06 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0035_socials'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='socials',
            options={'verbose_name': 'Социальная сеть', 'verbose_name_plural': 'Социальные сети'},
        ),
        migrations.AddField(
            model_name='socials',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/socials', verbose_name='Логотип Соцсети'),
        ),
        migrations.AlterField(
            model_name='socials',
            name='social_network',
            field=models.CharField(choices=[('IG', 'Instagram'), ('FB', 'Facebook'), ('VK', 'VK'), ('TG', 'Telegram')], max_length=30, verbose_name='Соцсеть'),
        ),
    ]