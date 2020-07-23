from django.views import View
from django.shortcuts import redirect
from store.models import Product
from cart.cart import Cart


class CartAddItem(View):
    """Add product to cart"""
    def get(self, request, id):
        cart = Cart(request)
        product = Product.objects.get(id=id)
        cart.add(product=product)
        return redirect("store:home_url")


class CartItemDelete(View):
    """Remove product from cart"""
    def get(self, request, id):
        cart = Cart(request)
        product = Product.objects.get(id=id)
        cart.remove(product)
        return redirect("store:home_url")
