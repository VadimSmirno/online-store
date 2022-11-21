from django.contrib.auth.models import User
from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='цена')
    pieces_left = models.IntegerField(verbose_name='Остаток')
    img = models.ImageField(blank=True, null=True, verbose_name='Изображение')
    number_of_sales = models.IntegerField(default=0,verbose_name='количество продаж')
    products_in_stock = models.BooleanField(default=True)
    free_delivery = models.BooleanField(default=False)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE,
                                         related_name='product',
                                         blank=True, null=True)
    subcategory = models.ForeignKey('Subcategory', on_delete=models.CASCADE,
                                         related_name='subcategory_product',
                                         blank=True, null=True)
    number_of_reviews = models.IntegerField(default=0,verbose_name='количество отзывов')
    date_of_creation = models.DateField(verbose_name='дата создания')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Товары'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Subcategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return  self.name

    class Meta:
        db_table = 'Подкатегория'
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

class Category(models.Model):
    name = models.CharField(max_length=50)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, blank=True, null=True, related_name='subcategory')


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Категории'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Reviews(models.Model):
    descriptions = models.TextField(verbose_name='Текст комментария')
    review_product = models.ManyToManyField(Product, related_name='product_review')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_article')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created']


    def __str__(self):
        return f'Отзыв № {self.id}'
