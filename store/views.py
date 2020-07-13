from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from store.models import Category, Product, Brand


class BrandsCatagoriesView:
    """returns all brands"""
    def get_brands(self):
        return Brand.objects.all()

    def get_categories(self):
        return Category.objects.all()


class HomeView(ListView):
    """Views for Home Page"""
    model = Product
    template_name = 'store/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories_list'] = Category.objects.all()
        context['popular_categories'] = Category.objects.all()[0:3]
        return context


class CategoryListView(BrandsCatagoriesView, ListView):
    """Views for Category"""
    model = Product
    template_name = 'store/store.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data()
    #     context['products_list'] = Product.objects.all()
    #     return context


class ProductDetailView(DetailView):
    """Detail Views for products"""
    model = Product
    slug_url_kwarg = 'url'
    slug_field = 'url'