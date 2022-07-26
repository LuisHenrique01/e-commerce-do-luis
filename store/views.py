from django.views.generic import TemplateView, ListView, DetailView
from store.models import Category, Product


class HomeView(TemplateView):
    template_name = "home.html"


class CategoryDetailView(DetailView):
    model = Category
    extra_context = {}
    slug_url_kwarg = 'category_slug'
    template_name = "store/products.html"

    def get_context_data(self, **kwargs):
        self.extra_context['products'] = Product.objects.filter(
            category__slug=self.kwargs.get(self.slug_url_kwarg))
        return super().get_context_data(**kwargs)
