from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class ProductsManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Category(models.Model):

    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("store:category_detail", args=[self.slug])

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
    image = models.ImageField(upload_to='images/',
                              default='images/default.png')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #Managers
    objects = models.Manager()
    products_actives = ProductsManager()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ('-created', )

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])

    def __str__(self):
        return self.title
