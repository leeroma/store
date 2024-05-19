from django import forms

from storeapp.models import Product, Category, Order, ProductInCart


class ProductForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price', 'quantity', 'image',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description')


class OrderForm(forms.ModelForm):
    product = forms.ModelMultipleChoiceField(queryset=ProductInCart.objects.all(), label='Продукт')
    phone_number = forms.CharField(label="Номер телефона",
                                   widget=forms.TextInput(attrs={'value': '+77', 'placeholder': '+7 712 345 67 89'}))

    class Meta:
        model = Order
        exclude = ['created_at', ]
