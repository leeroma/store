from django.contrib import admin

from storeapp.models import Product, Category


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


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)