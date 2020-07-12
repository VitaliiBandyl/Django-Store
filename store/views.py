from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from store.models import Category, Product


class HomeView(ListView):
    """Views for Home Page"""
    model = Product
    template_name = 'store/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories_list'] = Category.objects.all()[0:3]
        return context


class CategoryListView(ListView):
    """Views for Category"""