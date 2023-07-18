# Generated by Django 4.2.2 on 2023-07-18 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0045_alter_socials_social_network'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services_files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Наименование')),
                ('file', models.FileField(blank=True, null=True, upload_to='images/pricelists', verbose_name='Файл с прайс листом')),
            ],
            options={
                'verbose_name': 'Прайс лист',
                'verbose_name_plural': 'Прайс листы',
            },
        ),
    ]
