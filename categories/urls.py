from django.urls import path
from .views import CategoryDetail

urlpatterns = [
    path("categories/<int:pk>/", CategoryDetail.as_view(), name="category-detail"),
    path("categories/", CategoryDetail.as_view(), name="category-list-create"),
]
