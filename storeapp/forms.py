from django.forms import forms

from storeapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price', 'image', )
        exclude = ('created_at', )
