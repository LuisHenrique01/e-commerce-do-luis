from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from django.urls import reverse
from store.views import *
from store.models import Category, Product


class TestViews(TestCase):

    def setUp(self) -> None:
        User.objects.create(username='admin')
        self.factory = RequestFactory()
        self.client = Client()
        self.category1 = Category.objects.create(name='Veiculos',
                                                 slug='veiculos')
        self.category2 = Category.objects.create(name='Livros', slug='livros')
        self.product1 = Product.objects.create(category_id=1,
                                               title='Lancer',
                                               create_by_id=1,
                                               slug='lancer',
                                               price='200.99',
                                               image='lancer')
        self.product2 = Product.objects.create(category_id=2,
                                               title='Python Fluente',
                                               create_by_id=1,
                                               slug='python-fluente',
                                               price='88.99',
                                               image='python')

    def test_homepage_url(self) -> None:
        request = self.factory.get('/')
        response = HomeView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self) -> None:
        request = self.factory.get('/')
        response = HomeView.as_view()(request)
        response.render()
        html = response.content.decode('utf8')
        self.assertIn('<title>Bem vindo</title>', html)
        self.assertIn(str(self.category1), html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_all_products(self) -> None:
        request = self.factory.get('/loja/')
        response = ProductListView.as_view()(request)
        response.render()
        html = response.content.decode('utf8')
        self.assertIn(str(self.product1), html)
        self.assertIn(str(self.product2), html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_category_products(self) -> None:
        response = self.client.get(
            reverse('store:category_detail', args=[self.category1.slug]))
        html = response.content.decode('utf8')
        self.assertIn(str(self.product1), html)
        self.assertNotIn(str(self.product2), html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_product_detail(self) -> None:
        response = self.client.get(f'/item/{self.product1.slug}/')
        html = response.content.decode('utf8')
        self.assertIn(str(self.product1), html)
        self.assertIn(self.product1.manufacturer, html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)