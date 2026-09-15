from django.urls import path
from .views import (
    CustomOrderFormListView,
    CustomOrderFormCreateView,
    CustomOrderFormRetrieveView,
    CustomOrderFormDeleteView
)

urlpatterns = [
    path("custom-orders/", CustomOrderFormListView.as_view(), name="custom-order-list"),
    path("custom-orders/create/", CustomOrderFormCreateView.as_view(), name="custom-order-create"),
    path("custom-orders/<int:id>/", CustomOrderFormRetrieveView.as_view(), name="custom-order-retrieve"),
    path("custom-orders/<int:id>/delete/", CustomOrderFormDeleteView.as_view(), name="custom-order-delete"),
]