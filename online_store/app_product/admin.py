from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from . models import Product,Category,Subcategory, Reviews
from django.utils.safestring import mark_safe

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ['get_img', 'name', 'price', 'number_of_sales', 'product_category']

    def get_img(self,obj):
        return mark_safe(f'<img src={obj.img.url} width="50"')
    get_img.short_description ='Изображение'

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['name']

@admin.register(Subcategory)
class SubcategoryAdmin(TranslationAdmin):
    list_display = ['name']

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['author', 'created', 'descriptions',]