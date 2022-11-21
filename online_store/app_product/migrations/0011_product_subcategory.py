# Generated by Django 4.1 on 2022-09-13 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0010_alter_subcategory_options_alter_subcategory_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory_product', to='app_product.subcategory'),
        ),
    ]
