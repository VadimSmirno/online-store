from django import forms
from django.contrib.auth.models import User
from django.db.models import Min, Max
from .models import Product

class FilterForms(forms.Form):
    min_price_product = Product.objects.aggregate(Min('price'))
    max_price_product = Product.objects.aggregate(Max('price'))

    price = forms.CharField(required= False,max_length=10,widget=forms.TextInput(attrs={
        'class' : 'range-line',
        'id':'price',
        'name':'price',
        'input_type':'number',
        'data-type':'double',
        'data-min':min_price_product['price__min'],
        'data-max': max_price_product['price__max']
    }))
    name = forms.CharField(required= False,max_length=30, widget=forms.TextInput(attrs={

        'type':'text',
        'class':'form-input form-input_full',
        'id' : "title",
        'name' : "title",
        'placeholder' : "Название"
    }))
    products_in_stock = forms.BooleanField(required= False,
                                           widget=forms.CheckboxInput(attrs={'class': 'toggle',}))
    free_shipping = forms.BooleanField(required= False,
                                       widget=forms.CheckboxInput(attrs={'class': 'toggle'}))



class SortedForms(forms.Form):
    popularity = forms.BooleanField(required=False)
    reviews = forms.BooleanField(required=False)
    novelty = forms.BooleanField(required=False)
    price_sorted = forms.BooleanField(required=False)

class ReviewForms(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = False

    body = forms.CharField(widget=forms.TextInput(attrs={

    'class' : 'form-textarea',
    'name':'review',
    'id':'review',
    'placeholder':'Добавить отзыв'
    }))

    class Meta:
        model = User
        fields = ['email', 'first_name']
        widgets = {'email' : forms.EmailInput(attrs={'class':'form-input' ,'id':'email', 'name':'email', 'type':'text', 'placeholder':'ел.почта'}),
                   'first_name' : forms.TextInput(attrs={'class':'form-input', 'id':'name', 'name':'name', 'type':'text',  'placeholder':'Имя'})}