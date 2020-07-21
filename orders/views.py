from django.shortcuts import render, redirect
from django.views import View

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


class CreateOrderView(View):
    """Create order"""
    def get(self, request):
        cart = Cart(request)
        return render(request, 'orders/checkout.html', context={'cart': cart})

    def post(self, request):
        cart = Cart(request)
        form = OrderCreateForm(request.POST)
        if not cart.cart:
            return redirect('home_url')

        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            cart.clear()
            return render(request, 'orders/order_created.html', context={'order': order})