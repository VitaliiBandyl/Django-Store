from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'city',
                  'country', 'postal_code', 'telephone', 'order_notes', 'city']
