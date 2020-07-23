from django.test import TestCase
from django.urls import reverse
from store.models import Category, Brand, Product, Review


def create_product(title: str, brand: Brand, description: str, year: int, country: str,
                   price: float, category: Category, discount: int=0, draft: bool=False,
                   availability: bool=True, new: bool=True, top_selling: bool=True) -> Product:
    """Creates a product"""
    slug = f'{brand.url}-{title.lower()}'
    return Product.objects.create(title=title, brand=brand, description=description, year=year, country=country,
                                  price=price, category=category, discount=discount, slug=slug, draft=draft,
                                  image='image', availability=availability, new=new, top_selling=top_selling)


def create_brand(name: str) -> Brand:
    """Creates a brand"""
    return Brand.objects.create(name=name, url=name)


def create_category(name: str) -> Category:
    """Creates a category"""
    return Category.objects.create(name=name, url=name, image="image")


def create_review(email: str, name: str, text: str, product: Product) -> Review:
    """Creates a review to product"""
    return Review.objects.create(email=email, name=name, text=text, product=product)


class ProductModelTests(TestCase):

    def test_calculation_discount(self):
        """Checks the correctness of the discount calculation"""
        category = create_category('test_name')
        brand = create_brand('test_brand')
        product = create_product(title='test product', brand=brand, description='test', year=2020, country='Ukraine',
                                 price=100.00, category=category, discount=10)

        self.assertEqual(90.00, product.get_price_with_discount(),
                         f'Incorrect discount precalculated. Expected result is 90.00 but '
                         f'Actual result is {product.get_price_with_discount()}')

    def test_calculation_discount_without_discount(self):
        """Checks the correctness of the discount calculation when discount = 0"""
        category = create_category('test_name')
        brand = create_brand('test_brand')
        product = create_product(title='test product', brand=brand, description='test', year=2020, country='Ukraine',
                                 price=100.00, category=category, discount=0)

        self.assertEqual(100.00, product.get_price_with_discount(),
                         f'Incorrect discount precalculated. Expected result is 100.00 but '
                         f'Actual result is {product.get_price_with_discount()}')


class TestHomeView(TestCase):

    def test_draft_false_question(self):
        """Product with mark draft=False is displayed on the index page."""
        category = create_category('test_name')
        brand = create_brand('Draft')
        product = create_product(title='False', brand=brand, description='test', year=2020, country='Ukraine',
                                 price=100.00, category=category, draft=False)

        response = self.client.get(reverse('home_url'))
        self.assertQuerysetEqual(
            response.context['product_list'],
            ['<Product: Draft False>']
        )

    def test_draft_true_question(self):
        """Product with mark draft=True is not displayed on the index page."""
        category = create_category('test_name')
        brand = create_brand('Draft')
        product = create_product(title='True', brand=brand, description='test', year=2020, country='Ukraine',
                                 price=100.00, category=category, draft=True)

        response = self.client.get(reverse('home_url'))
        self.assertQuerysetEqual(response.context['product_list'], [])

    def test_product_draft_false_and_true(self):
        """Product with mark draft=True is not displayed on the index page.
           Product with mark draft=False is displayed on the index page."""
        category = create_category('test_name')
        brand = create_brand('Draft')
        product_1 = create_product(title='True', brand=brand, description='test', year=2020, country='Ukraine',
                                   price=100.00, category=category, draft=True)
        product_2 = create_product(title='False', brand=brand, description='test', year=2020, country='Ukraine',
                                   price=100.00, category=category, draft=False)

        response = self.client.get(reverse('home_url'))
        self.assertQuerysetEqual(
            response.context['product_list'],
            ['<Product: Draft False>']
        )

    def test_two_products_draft_false(self):
        """The index page may display multiple products."""
        category = create_category('test_name')
        brand = create_brand('brand')
        product_1 = create_product(title='One', brand=brand, description='test', year=2020, country='Ukraine',
                                   price=100.00, category=category, draft=False)
        product_2 = create_product(title='Two', brand=brand, description='test', year=2020, country='Ukraine',
                                   price=100.00, category=category, draft=False)

        response = self.client.get(reverse('home_url'))
        self.assertQuerysetEqual(
            response.context['product_list'],
            ['<Product: brand One>', '<Product: brand Two>'], ordered=False
        )


class ProductDetailViewTests(TestCase):

    def test_draft_true_product(self):
        """The detail view of a product with a draft=True returns a 404 not found."""
        category = create_category('test_name')
        brand = create_brand('Draft')
        product = create_product(title='True', brand=brand, description='test', year=2020, country='Ukraine',
                                 price=100.00, category=category, draft=True)

        url = reverse('product_detail_url', args=(category.url, product.slug))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_draft_false_product(self):
        """The detail view of a product with a draft=True returns a 404 not found."""
        category = create_category('test_name')
        brand = create_brand('Draft')
        product = create_product(title='False', brand=brand, description='test', year=2020, country='Ukraine',
                                 price=100.00, category=category, draft=False)

        url = reverse('product_detail_url', args=(category.url, product.slug))
        response = self.client.get(url)
        self.assertContains(response, product.title)
        self.assertEqual(response.status_code, 200)
