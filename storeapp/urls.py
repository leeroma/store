from django.urls import path

from storeapp.views import products_view, categories_view, category_add_view, product_add_view, product_view


urlpatterns = [
    path('', products_view, name='products'),
    path('products', products_view, name='products'),
    path('categories', categories_view, name='categories'),
    path('product/<int:pk>', product_view, name='product'),
    path('categories/add', category_add_view, name='category_add'),
    path('products/add', product_add_view, name='product_add'),
]
