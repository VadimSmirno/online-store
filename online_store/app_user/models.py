from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    avatar_img = models.ImageField(blank=True, null=True, verbose_name='Аватарка')
    middle_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Отчество')
    number_phone = models.CharField(max_length=10, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_info')

    def __str__(self):
        return f'{self.user}'

    class Meta():
        db_table = 'Профайл'
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'
