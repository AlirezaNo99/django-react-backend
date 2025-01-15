from django.urls import path
from .views import PostDetail,PostCount,PostListByCategory

urlpatterns = [
    path("posts/<int:pk>/", PostDetail.as_view(), name="post-detail"),
    path("posts/", PostDetail.as_view(), name="post-create"),
    path('posts/count/', PostCount.as_view(), name='post-count'),
    path(
        "posts/category/<int:category_id>/",
        PostListByCategory.as_view(),
        name="posts-list-by-category"
    ),  # Query params: ?min_price=0&max_price=100&sort_by=price

    # URL for fetching products by multiple category IDs (via query parameters)
    path('posts/categories/', PostListByCategory.as_view(), name='post-list-by-multiple-categories'),
]
