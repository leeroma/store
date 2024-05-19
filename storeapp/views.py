from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from storeapp.forms import ProductForm, CategoryForm
from storeapp.models import Product, Category


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'index.html'
    paginate_by = 4
    paginate_orphans = 2

    filter_value = None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        context['name'] = self.filter_value
        return context

    def get(self, request, *args, **kwargs):
        self.filter_value = self.request.GET.get('name')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.filter_value:
            queryset = queryset.filter(category__name=self.filter_value)

        return queryset


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product, pk=self.kwargs['pk'])
        return context


class CategoriesListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'categories.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class CreateCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_add.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('categories'))


class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_add.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return HttpResponseRedirect(reverse('product', args=[product.pk]))

        return render(request, self.template_name, {'form': form})


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_edit.html'
    context_object_name = 'category'

    def get_success_url(self):
        return reverse('categories')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_edit.html'
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('product', args=[self.get_object().pk])


class CategoryDeleteView(DeleteView):
    model = Category

    def get_success_url(self):
        return reverse('categories')


class ProductDeleteView(DeleteView):
    model = Product

    def get_success_url(self):
        return reverse('products')
