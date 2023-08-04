from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Ваше Имя')
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Ваш номер телефона')
    # message = forms.CharField(max_length=600, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Введите сообщение')
