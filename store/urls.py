from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home_url'),
    path('<slug:category>/<slug:url>/', views.ProductDetailView.as_view(), name='product_detail_url'),
    path('product_list/', views.ProductListView.as_view(), name='product_list_url'),
]
