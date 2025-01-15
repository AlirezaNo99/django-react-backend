from django.urls import path
from .views import SubscribeAPIView, UnsubscribeAPIView

urlpatterns = [
    path('newsLetter/subscribe/', SubscribeAPIView.as_view(), name='subscribe'),
    path('newsLetter/unsubscribe/', UnsubscribeAPIView.as_view(), name='unsubscribe'),
]
