from django.views import View
from django.shortcuts import render, redirect
from store.models import Product
from cart.cart import Cart


class CartDetailView(View):
    """Cart View"""
    def get(self, request):
        return render(request, 'cart/checkout.html')


class CartAddItem(View):
    """Add product to cart"""
    def get(self, request, id):
        cart = Cart(request)
        product = Product.objects.get(id=id)
        cart.add(product=product)
        return redirect("home_url")


class CartItemDelete(View):
    """Remove product from cart"""
    def get(self, request, id):
        cart = Cart(request)
        product = Product.objects.get(id=id)
        cart.remove(product)
        return redirect("home_url")
