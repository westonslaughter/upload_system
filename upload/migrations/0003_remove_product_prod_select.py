# Generated by Django 4.1.6 on 2023-02-24 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_alter_product_prod_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='prod_select',
        ),
    ]
