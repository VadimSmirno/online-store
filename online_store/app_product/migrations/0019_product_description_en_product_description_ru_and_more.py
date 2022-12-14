# Generated by Django 4.1 on 2022-10-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0018_alter_reviews_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=30, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(max_length=30, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]
