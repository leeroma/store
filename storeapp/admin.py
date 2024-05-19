from django.contrib import admin

from storeapp.models import Product, Category, ProductInCart, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('category',)
    search_fields = ('name', 'category', 'price',)
    exclude = []
    readonly_fields = ('created_at',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    exclude = []


class ProductInCartAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity',)
    search_fields = ('product', 'quantity',)
    exclude = []


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'phone_number', 'created_at', )
    search_fields = ('id', 'client_name', 'phone_number',)
    exclude = []
    readonly_fields = ('created_at',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductInCart, ProductInCartAdmin)
admin.site.register(Order, OrderAdmin)
