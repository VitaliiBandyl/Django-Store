from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Categories"""
    name = models.CharField("Category", max_length=150, unique=True)
    url = models.SlugField(max_length=150, unique=True)
    image = models.ImageField("Image", upload_to="category_images/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse('category_list_url')


class Brand(models.Model):
    """Brand"""
    name = models.CharField("Brand", max_length=150, unique=True)
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class Product(models.Model):
    """Goods"""
    title = models.CharField("Title", max_length=100, db_index=True)
    brand = models.ForeignKey(Brand, verbose_name="Brand", on_delete=models.CASCADE, null=True)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="product_images/")
    year = models.PositiveSmallIntegerField("Year", default=2020)
    country = models.CharField("Country", max_length=30)
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField("Draft", default=False)
    availability = models.BooleanField("Availability", default=True)
    new = models.BooleanField('New', default=True)
    top_selling = models.BooleanField('Top Selling', default=False)
    discount = models.SmallIntegerField('Discount', default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug': self.slug, 'category': self.category})

    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={
            'slug': self.slug
        })

    def get_price_with_discount(self):
        return self.price / 100 * (100 - self.discount)

    def __str__(self):
        return f'{self.brand} {self.title}'

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductShot(models.Model):
    """Frames from the movie"""
    title = models.CharField("Title", max_length=100)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="product_shots/")
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Additional product image"
        verbose_name_plural = "Additional product images"



class Review(models.Model):
    """Review"""
    email = models.EmailField()
    name = models.CharField("Name", max_length=100)
    text = models.TextField("Message", max_length=5000)
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Review"
