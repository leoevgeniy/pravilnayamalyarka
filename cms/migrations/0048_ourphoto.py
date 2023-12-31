# Generated by Django 4.2.2 on 2023-07-25 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0047_service_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Наименование')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/donework', verbose_name='Наши фото')),
            ],
            options={
                'verbose_name': 'Наши фото',
                'verbose_name_plural': 'Наши фото',
            },
        ),
    ]
