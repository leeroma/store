from django import forms

from storeapp.models import Product, Category


class ProductForm(forms.ModelForm):

    image = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price', 'image', )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description')
