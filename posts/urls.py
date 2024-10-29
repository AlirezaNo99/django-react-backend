from django.urls import path
from .views import PostDetail,PostCount

urlpatterns = [
    path("posts/<int:pk>/", PostDetail.as_view(), name="post-detail"),
    path("posts/", PostDetail.as_view(), name="post-create"),
    path('posts/count/', PostCount.as_view(), name='post-count'),

]
