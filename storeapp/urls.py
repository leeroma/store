from django.urls import path

from storeapp.views import ProductListView, categories_view, category_add_view, category_edit_view, CreateProductView, \
    ProductDetailView, category_delete_view, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('products', ProductListView.as_view(), name='products'),
    path('categories', categories_view, name='categories'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('categories/add', category_add_view, name='category_add'),
    path('categories/<int:pk>/edit', category_edit_view, name='category_edit'),
    path('products/<int:pk>/edit', ProductUpdateView.as_view(), name='product_edit'),
    path('categories/<int:pk>/delete', category_delete_view, name='category_delete'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('products/add', CreateProductView.as_view(), name='product_add'),
]
