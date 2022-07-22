from email.mime import image
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(Category,
                                 related_name='product',
                                 on_delete=models.CASCADE)
    create_by = models.ForeignKey(User,
                                  related_name='product_create',
                                  on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255, default='Luis Develop')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ('-created', )

    def __str__(self):
        return self.title
