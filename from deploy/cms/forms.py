from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()


class SearchForm(forms.Form):
    text = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'input-search', 'id': 'search-input', 'type': 'search', 'placeholder': 'Поиск товара'}),
                           label='')
