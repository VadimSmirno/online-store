from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs=
                                                     {
                                                         'placeholder': 'Email'
                                                     }))


    class Meta:
        model = User
        fields = ['username', 'email', ]
        help_texts = {
            'username': None,
        }
        labels = {
            'username' : '',

        }
        widgets = {
            'username' : forms.TextInput(attrs=
                                         {
                                             'placeholder': 'username'
                                         })
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        


class ProfileRedactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        last_name = kwargs['initial']['last_name']
        first_name = kwargs['initial']['first_name']
        email = kwargs['initial']['email']
        middle_name = kwargs['initial']['middle_name']
        avatar_img = kwargs['initial']['avatar_img']
        number_phone = kwargs['initial']['number_phone']

        self.fields['name'].widget = forms.TextInput(attrs={
            'class': 'form-input',
            'id': 'name',
            'type': 'text',
            'data-validate': 'require',
            'value': f'{last_name} {first_name} {middle_name}'
        })

        self.fields['email'].widget = forms.TextInput(attrs={
            'class': 'form-input',
            'id': 'mail',
            'name': 'mail',
            'type': 'text',
            'value': f'{email}',
            'data-validate': 'require'})

        self.fields['photo_avatar'].widget = forms.FileInput(attrs={
            'class': 'Profile-file form-input',
            'type': 'file',
            'data - validate': 'onlyImgAvatar',

        })
        self.fields['number_phone'].widget = forms.TextInput(attrs={
            'class': 'form-input',
            'id': 'phone',
            'name': 'phone',
            'type': 'text',
            'value': number_phone})

    name = forms.CharField(max_length=30)
    number_phone = forms.CharField(validators=[RegexValidator(
        "^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$",
        message='Пожалуйста, введите номер мобильного телефона в правильном формате! ')])

    email = forms.EmailField()
    password1 = forms.CharField(max_length=100, required=False, widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'id': 'password',
        'name': 'password',
        'type': 'password',
        'placeholder': 'Тут можно изменить пароль'}))
    password2 = forms.CharField(max_length=100, required=False, widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'id': 'passwordReply',
        'name': 'passwordReply',
        'type': 'password',
        'placeholder': 'Введите пароль повторно'}))
    photo_avatar = forms.ImageField(required=False)

    def clean(self):
        super().clean()
        cleaned_data = self.cleaned_data
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Пароли должны быть одинаковыми")
        else:
            return cleaned_data


    def clean_name(self):
        super().clean()
        name = self.cleaned_data.get('name')
        name = name.split(' ')
        if len(name) != 3:
            raise forms.ValidationError(message='Введите ФИО полностью через пробел')
        return name

    
