from app_user.forms import UserRegistrationForm
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django import forms
from django.utils.translation import gettext_lazy as _



class UserInfoForm(UserRegistrationForm,UserCreationForm):
    telephone_number = forms.CharField(validators=[RegexValidator(
        "^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$",
        message='Пожалуйста, введите номер мобильного телефона в правильном формате! ')], widget=forms.TextInput(attrs={

    'class': 'form-input', 'id':'phone', 'name':'phone', 'type':'text', 'value':'+70000000000'
        }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-input',
        'id': 'mail', 'name': 'mail',
        'type': 'text', 'value': "email",
        'data-validate': 'require'}))

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class' :'form-input',
                'id':'password',
                'name':'password',
                'type':'password',
                'placeholder':'Ведите пароль'}),
        help_text=password_validation.password_validators_help_text_html())

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class' :'form-input',
                'id':'passwordReply',
                'name':'passwordReply',
                'type':'password',
                'placeholder':'Введите пароль повторно'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )


    class Meta(UserRegistrationForm.Meta):
        widgets = {
            'username' : forms.HiddenInput(attrs={
            'class' :'form-input',
                'id':'name', 'name':'name',
                'type':'text',
                'value' : 'user',
                'data - validate' : 'require',

        }),

        }

class CartNumberForm(forms.Form):
    number = forms.IntegerField(max_value=999999999, min_value=100000000,
                                widget=forms.NumberInput(attrs={

    'class':'form-input Payment-bill',
        'id':'numero1',
        'name':'numero1',
        'type':'text',
        'placeholder':'9999 9999',
        'data-mask':'99999999',

    }))