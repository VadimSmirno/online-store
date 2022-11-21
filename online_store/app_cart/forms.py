from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label='', widget=forms.TextInput(
        attrs={'class': 'Amount-input form-input', 'value': 1, 'name': 'amount'}))
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
