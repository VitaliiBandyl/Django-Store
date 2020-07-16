from django.urls import path
from . import views


urlpatterns = [
    path('add/<int:id>/', views.CartAddItem.as_view(), name='cart_add'),
    path('item_clear/<int:id>/', views.CartItemDelete.as_view(), name='item_clear'),
]