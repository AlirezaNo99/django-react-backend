from django.urls import path
from .views import DigitalProductDetail, DigitalProductCount,DigitalProductListByCategory

urlpatterns = [
    path("digitalProducts/<int:pk>/", DigitalProductDetail.as_view(), name="digitalProduct-detail"),
    path("digitalProducts/", DigitalProductDetail.as_view(), name="digitalProduct-create"),
    path('digitalProducts/count/', DigitalProductCount.as_view(), name='digital-product-count'),
    path('digitalProducts/category/<int:category_id>/', DigitalProductListByCategory.as_view(), name='digitalProduct-list-by-category'),


]