from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view()),

    path('<slug:category>/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail_url'),
    path('<slug:slug>/', views.CategoryListView.as_view(), name='category_list_url'),
]
