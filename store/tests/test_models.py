from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self) -> None:
        self.category1 = Category.objects.create(name="Veiculos",
                                                 slug="veiculos")

    def test_category_model_entry(self) -> None:
        category1 = self.category1
        self.assertTrue(isinstance(category1, Category))

    def test_category_model_str_representation(self) -> None:
        category1 = self.category1
        self.assertEqual(str(category1), 'Veiculos')


class TestProductsModel(TestCase):

    def setUp(self) -> None:
        Category.objects.create(name="Veiculos", slug="veiculos")
        User.objects.create(username='admin')
        self.product1 = Product.objects.create(category_id=1,
                                               title='Lancer',
                                               create_by_id=1,
                                               slug='lancer',
                                               price='200.99',
                                               image='lancer')

    def test_products_model_entry(self) -> None:
        product1 = self.product1
        self.assertTrue(isinstance(product1, Product))

    def test_products_model_str_representation(self) -> None:
        product1 = self.product1
        self.assertEqual(str(product1), 'Lancer')