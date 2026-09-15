from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import CustomOrderForm
from .serializers import CustomOrderFormSerializer, CustomOrderFormSerializerList

class CustomOrderPagination(PageNumberPagination):
    page_size = 10  # Default items per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class CustomOrderFormListView(generics.ListAPIView):
    """List all custom orders with pagination"""
    queryset = CustomOrderForm.objects.all().order_by('-created_at')
    serializer_class = CustomOrderFormSerializerList
    pagination_class = CustomOrderPagination  # Add pagination here

class CustomOrderFormCreateView(generics.CreateAPIView):
    """Create a new custom order"""
    queryset = CustomOrderForm.objects.all()
    serializer_class = CustomOrderFormSerializer

class CustomOrderFormRetrieveView(generics.RetrieveAPIView):
    """Retrieve a single custom order by ID"""
    queryset = CustomOrderForm.objects.all()
    serializer_class = CustomOrderFormSerializer
    lookup_field = "id"

class CustomOrderFormDeleteView(generics.DestroyAPIView):
    """Delete a custom order by ID"""
    queryset = CustomOrderForm.objects.all()
    serializer_class = CustomOrderFormSerializer
    lookup_field = "id"