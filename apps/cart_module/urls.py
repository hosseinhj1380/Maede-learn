from django.urls import path
from .views import AddToCartView, CartView, RemoveFromCartView

urlpatterns = [
    path('shopping-cart', CartView.as_view(), name='cart'),
    path('shopping-cart/add/<int:pk>/', AddToCartView.as_view(), name='add-to-cart'),
    path('shopping-cart/remove/<int:pk>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
]
