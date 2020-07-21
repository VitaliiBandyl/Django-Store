from django.db.models import Q
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, DetailView

from store.models import Category, Product, Brand
from .forms import ReviewForm


class BrandsCategories:
    """returns all brands"""
    def get_brands(self):
        return Brand.objects.all()

    def get_categories(self):
        return Category.objects.all()


class HomeView(ListView):
    """Views for Home Page"""
    template_name = 'store/index.html'
    queryset = Product.objects.filter(draft=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories_list'] = Category.objects.filter(product__draft=False)
        context['popular_categories'] = Category.objects.filter(product__draft=False)[0:3]
        return context


class ProductListView(BrandsCategories, ListView):
    """Views for Category"""

    def get_queryset(self):
        queryset = Product.objects.all()
        if self.request.GET.getlist('brand'):
            queryset = queryset.filter(brand__in=self.request.GET.getlist('brand'))

        if self.request.GET.getlist('category'):
            queryset = queryset.filter(category__in=self.request.GET.getlist('category'))

        if self.request.GET.getlist('price-min'):
            queryset = queryset.filter(price__gte=self.request.GET.get('price-min'))

        if self.request.GET.getlist('price-max'):
            queryset = queryset.filter(price__lte=self.request.GET.get('price-max'))

        return queryset.filter(draft=False)


class ProductDetailView(DetailView):
    """Detail Views for products"""
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        current_category = self.kwargs.get('category')
        context['related_products'] = Product.objects.filter(category__name=current_category)
        return context


class SearchView(ListView):
    """Search"""

    def get_queryset(self):
        queryset =  Product.objects.filter(
            Q(title__icontains=self.request.GET.get("q"))|
            Q(brand__name__icontains=self.request.GET.get("q"))
        ).filter(draft=False).distinct()

        return queryset


class AddReview(View):
    """Add Review to product"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = product
            form.save()
        return redirect(product.get_absolute_url())
