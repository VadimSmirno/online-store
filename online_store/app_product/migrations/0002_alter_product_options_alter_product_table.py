# Generated by Django 4.1 on 2022-08-30 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelTable(
            name='product',
            table='Товары',
        ),
    ]