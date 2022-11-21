from django.contrib.auth.models import User
from django.db import models
from app_product.models import Product

class Order(models.Model):
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    payment_method = models.CharField(max_length=50)
    delivery_method = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_order',null=True, blank=True)
    count_product = models.IntegerField(default=0)
    number_order = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='общая стоимость', default=0.00)
    status = models.BooleanField(default=False, null=True, blank=True)
    text_error = models.TextField(null=True, blank=True)
    code_error = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    def __str__(self):
        return f'Order {self.id}'

