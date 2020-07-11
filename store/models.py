from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Categories"""
    name = models.CharField("Category", max_length=150)
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Subcategory(models.Model):
    """Subcategories"""
    name = models.CharField("Subcategory", max_length=150)
    url = models.SlugField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,  null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"


class Product(models.Model):
    """Goods"""
    title = models.CharField("Title", max_length=100)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="images/")
    year = models.PositiveSmallIntegerField("Made date", default=2020)
    country = models.CharField("Country", max_length=30)
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    subcategory = models.ForeignKey(Subcategory, verbose_name="Subcategory", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField("Draft", default=False)
    availability = models.BooleanField("Availability", default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug': self.url})

    def __str__(self):
        return self.title

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


class RatingStar(models.Model):
    """Rating stars"""
    value = models.SmallIntegerField("Star", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Rating Star"
        verbose_name_plural = "Rating Stars"


class Rating(models.Model):
    """Rating"""
    ip = models.CharField("IP address", max_length=15)
    star = models.ForeignKey(RatingStar, verbose_name="Rating Star", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.star} - {self.product}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


class Reviews(models.Model):
    """Reviews"""
    email = models.EmailField()
    name = models.CharField("Name", max_length=100)
    text = models.TextField("Message", max_length=5000)
    product = models.ForeignKey(Product, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

