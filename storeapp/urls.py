from django.urls import path

from storeapp.views import ProductListView, CategoriesListView, CreateCategoryView, CategoryUpdateView, \
    CreateProductView, ProductDetailView, CategoryDeleteView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('products', ProductListView.as_view(), name='products'),
    path('categories', CategoriesListView.as_view(), name='categories'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('categories/add', CreateCategoryView.as_view(), name='category_add'),
    path('categories/<int:pk>/edit', CategoryUpdateView.as_view(), name='category_edit'),
    path('products/<int:pk>/edit', ProductUpdateView.as_view(), name='product_edit'),
    path('categories/<int:pk>/delete', CategoryDeleteView.as_view(), name='category_delete'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('products/add', CreateProductView.as_view(), name='product_add'),
]
