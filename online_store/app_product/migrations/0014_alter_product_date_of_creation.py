# Generated by Django 4.1 on 2022-09-21 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0013_product_date_of_creation_product_number_of_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_of_creation',
            field=models.DateField(verbose_name='дата создания'),
        ),
    ]