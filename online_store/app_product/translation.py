from modeltranslation.translator import translator, TranslationOptions
from .models import Product, Category, Subcategory

class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

translator.register(Product, ProductTranslationOptions)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Category, CategoryTranslationOptions)

class SubcategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Subcategory, SubcategoryTranslationOptions)
