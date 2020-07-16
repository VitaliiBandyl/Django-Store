from decimal import Decimal

from django.conf import settings

from store.models import Product


class Cart:
    """Shopping cart"""
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, action=None):
        """Add a product to the cart or update its quantity."""
        id = product.id
        new_item = True
        if str(product.id) not in self.cart.keys():

            self.cart[product.id] = {
                'userid': self.request.user.id,
                'product_id': id,
                'name': product.title,
                'quantity': 1,
                'price': str(product.price),
                'image': product.image.url
            }
        else:
            new_item = True

            for key, value in self.cart.items():
                if key == str(product.id):

                    value['quantity'] = value['quantity'] + 1
                    new_item = False
                    self.save()
                    break
            if new_item == True:

                self.cart[product.id] = {
                    'userid': self.request.user,
                    'product_id': product.id,
                    'name': product.title,
                    'quantity': 1,
                    'price': str(product.price),
                    'image': product.image.url
                }
        self.save()

    def save(self):
        """update the session cart"""
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        """Remove a product from the cart."""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        """Remove all items from cart"""
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def __iter__(self):
        """Iterates items in the cart and retrieving products from the database."""
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """Counts the number of items in the cart"""
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """Calculate cart total amount."""
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())
