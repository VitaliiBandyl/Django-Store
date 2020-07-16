from django.db import models
from store.models import Product


class Order(models.Model):
    """Order model"""
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name',max_length=50)
    email = models.EmailField()
    address = models.CharField('Address',max_length=250)
    city = models.CharField('City', max_length=100)
    country = models.CharField('Country', max_length=50)
    telephone = models.CharField('Telephone', max_length=15)
    postal_code = models.CharField('Postal Code', max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField('Pay Status', default=False)
    order_notes = models.CharField('Additional information', max_length=2000)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """Order item"""
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity
