from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=100, blank=False, null=False)
    description = models.TextField('Описание', max_length=3000, blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('Название', max_length=100, blank=False, null=False)
    description = models.TextField('Описание', max_length=3000, blank=True)
    category = models.ManyToManyField(Category, verbose_name='Категория', related_name='category')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    quantity = models.DecimalField('Количество', max_digits=5, decimal_places=0, default=1,
                                   validators=[MinValueValidator(1)])
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    image = models.ImageField('Изображение', upload_to='products')

    @property
    def get_category(self):
        categories = self.category.all()
        if categories:
            return ','.join([category.name for category in categories])

        return 'Товар без категории'

    def __str__(self):
        return self.name


class ProductInCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Корзина')
    quantity = models.DecimalField('Количество', max_digits=5, decimal_places=0, default=1,
                                   validators=[MinValueValidator(1)])

    class Meta:
        verbose_name_plural = 'Products in cart'

    def __str__(self):
        return self.product.name


class Order(models.Model):
    product = models.ManyToManyField(Product, verbose_name='Заказ', related_name='order')
    client_name = models.CharField('Имя пользователя', max_length=200, blank=False, null=False)
    phone_number = models.CharField('Телефон', max_length=13, blank=False, null=False)
    address = models.CharField('Адрес', max_length=200, blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
