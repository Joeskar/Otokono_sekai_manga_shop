from django.urls import path
from apps.cart.views import CartView, AddToCartView, RemoveFromCartView, OrderView

urlpatterns = [
    path('cart_list/', CartView.as_view(), name='cart'),
    path('add/<slug:product_slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove/<slug:product_slug>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('checkout/', OrderView.as_view(), name='checkout')
]