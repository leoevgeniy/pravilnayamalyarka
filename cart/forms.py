from django import forms


class OrderConfirmForm(forms.Form):
    name = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Имя')
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Телефон')
