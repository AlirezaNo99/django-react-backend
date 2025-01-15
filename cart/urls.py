from django.urls import path
from .views import add_to_cart, remove_from_cart, view_cart, update_cart_item

urlpatterns = [
    path('cart/add/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/view/', view_cart, name='view_cart'),
    path('cart/update/<int:product_id>/', update_cart_item, name='update_cart_item'),  # New endpoint
]