# Generated by Django 4.1 on 2022-09-23 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0002_alter_profile_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='number_phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
