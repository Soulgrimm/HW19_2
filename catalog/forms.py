from django import forms

from catalog.models import Product, Version


class StyleForMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleForMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'purchase_price', 'category',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if cleaned_data in [
            'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
            raise forms.ValidationError('Наименование содержит запрещенные слова')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        if cleaned_data in [
            'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
            raise forms.ValidationError('Описание содержит запрещенные слова')

        return cleaned_data


class VersionForm(StyleForMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
