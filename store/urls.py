from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view()),
    path('<slug:slug>/', views.CategoryListView.as_view(), name='category_list_view'),
]
