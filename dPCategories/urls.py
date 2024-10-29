from django.urls import path
from .views import DPCategoryDetail,DPCategoryCount

urlpatterns = [
    path("dPCategories/<int:pk>/", DPCategoryDetail.as_view(), name="dpCategory-detail"),
    path("dPCategories/", DPCategoryDetail.as_view(), name="dpCategory-list-create"),
    path('categories/count/', DPCategoryCount.as_view(), name='category-count'),

]
