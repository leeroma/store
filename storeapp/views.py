from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from storeapp.forms import ProductForm, CategoryForm
from storeapp.models import Product, Category, ProductInCart


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'index.html'
    ordering = ('name',)
    paginate_by = 4
    paginate_orphans = 2

    filter_value = None
    search_value = None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        context['name'] = self.filter_value
        return context

    def get(self, request, *args, **kwargs):
        self.filter_value = self.request.GET.get('name')
        self.search_value = self.request.GET.get('search')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset().filter(quantity__gt=0)
        if self.filter_value:
            queryset = queryset.filter(category__name=self.filter_value)

        if self.search_value:
            queryset = queryset.filter(
                Q(name__icontains=self.search_value) |
                Q(price__icontains=self.search_value)
            )

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


class ProductInCartView(TemplateView):
    model = ProductInCart
    template_name = 'cart.html'
    context_object_name = 'cart'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.model.objects.all()
        return context


class AddToCartView(TemplateView):
    model = ProductInCart

    product = None
    quantity = 0

    def get(self, request, *args, **kwargs):
        self.product = get_object_or_404(Product, pk=self.kwargs['pk'])
        self.quantity = int(request.GET['qty'])
        self.add_to_cart()

        return HttpResponseRedirect(reverse('cart'))

    def add_to_cart(self):
        if ProductInCart.objects.filter(product_id=self.product.pk).exists():
            cart_product = ProductInCart.objects.get(product_id=self.product.pk)
            cart_product.quantity += self.quantity
            self.product.quantity -= self.quantity
            cart_product.save()
            self.product.save()

        elif self.product.quantity > 0:
            self.product.quantity -= self.quantity
            self.product.save()
            cart_product = ProductInCart.objects.create(product=self.product, quantity=self.quantity)
            cart_product.save()

        else:
            return HttpResponseRedirect(reverse('products'))


class DeleteFromCartView(DeleteView):
    model = ProductInCart

    def get_success_url(self):
        return reverse('cart')

    def post(self, request, *args, **kwargs):
        product_in_cart = get_object_or_404(ProductInCart, pk=self.kwargs['pk'])
        product = get_object_or_404(Product, pk=product_in_cart.product_id)
        success_url = self.get_success_url()
        product.quantity += product_in_cart.quantity
        product.save()
        product_in_cart.delete()
        return HttpResponseRedirect(success_url)


