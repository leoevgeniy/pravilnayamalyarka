# Generated by Django 4.2.2 on 2023-07-06 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0034_alter_introduction_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Socials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_network', models.CharField(choices=[('IG', 'Instagram'), ('FB', 'Facebook'), ('VK', 'VK')], max_length=30, verbose_name='Соцсеть')),
                ('link', models.CharField(max_length=250, verbose_name='Ссылка на социальную сеть')),
            ],
        ),
    ]
