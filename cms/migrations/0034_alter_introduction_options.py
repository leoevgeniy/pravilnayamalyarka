# Generated by Django 4.2.2 on 2023-07-06 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0033_alter_introduction_options_alter_introduction_inuse_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='introduction',
            options={'verbose_name': 'О компании', 'verbose_name_plural': 'О компании'},
        ),
    ]
