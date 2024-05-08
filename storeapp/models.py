from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=100, blank=False, null=False)
    description = models.TextField('Описание', max_length=3000, blank=True)


class Product(models.Model):
    name = models.CharField('Название', max_length=100, blank=False, null=False)
    description = models.TextField('Описание', max_length=3000, blank=True)
    category = models.ManyToManyField(Category, verbose_name='Категория', related_name='category', blank=False)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    image = models.ImageField('Изображение', upload_to='products')