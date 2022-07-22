from django.views.generic import ListView
from .models import Product


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = "home.html"
