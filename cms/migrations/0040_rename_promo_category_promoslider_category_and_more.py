# Generated by Django 4.2.2 on 2023-07-12 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0039_contacts_email1_contacts_email2_contacts_email3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promoslider',
            old_name='promo_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='promoslider',
            old_name='promo_subcategory',
            new_name='subcategory',
        ),
    ]
