from django.urls import path
from .views import get_payment_token

urlpatterns = [
    path('orders/getPaymentToken/', get_payment_token, name='get_payment_token'),
]