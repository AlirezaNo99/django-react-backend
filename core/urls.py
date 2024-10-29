from django.urls import path
from .views import GlobalSearchView

urlpatterns = [
    path('searchPostsAndProducts/', GlobalSearchView.as_view(), name='global-search'),
]