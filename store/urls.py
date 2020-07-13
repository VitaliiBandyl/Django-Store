from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home_url'),
    path('<slug:category>/<slug:url>/', views.ProductDetailView.as_view(), name='product_detail_url'),
    path('categories/', views.CategoryListView.as_view(), name='category_list_url'),
]
