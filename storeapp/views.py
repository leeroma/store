from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from storeapp.forms import ProductForm, CategoryForm
from storeapp.models import Product, Category


def products_view(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    if not categories:
        return redirect('category_add')

    if not products:
        return redirect('product_add')

    return render(request, 'index.html', context={'products': products})


def product_view(request, pk: int):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={'product': product})


def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', context={'categories': categories})


def category_add_view(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('product'))

    return render(request, 'category_add.html', context={'form': form})


def product_add_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return HttpResponseRedirect(reverse('product', args=[product.pk]))

    return render(request, 'product_add.html', context={'form': form})


def category_edit_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('categories'))

    return render(request, 'category_edit.html', context={'category': category, 'form': form})


def category_delete_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return HttpResponseRedirect(reverse('categories'))