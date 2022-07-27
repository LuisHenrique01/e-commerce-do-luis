from django.urls import path
from .views import HomeView, CategoryDetailView, ProductDetailView

app_name = 'store'

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('loja/<slug:category_slug>/',
         CategoryDetailView.as_view(),
         name='category_detail'),
    path('item/<slug:slug>/',
         ProductDetailView.as_view(),
         name='product_detail')
]
