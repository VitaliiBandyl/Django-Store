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


class ProductListView(BrandsCatagoriesView, ListView):
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

        return queryset


class ProductDetailView(DetailView):
    """Detail Views for products"""
    model = Product
    slug_url_kwarg = 'url'
    slug_field = 'url'