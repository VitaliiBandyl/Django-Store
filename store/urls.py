from django.urls import path
from . import views


app_name = 'store'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_url'),
    path('product_list/', views.ProductListView.as_view(), name='product_list_url'),
    path("search/", views.SearchView.as_view(), name='search'),
    path('review/<int:pk>/', views.AddReview.as_view(), name="add_review"),
    path('<slug:category>/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail_url'),
]
