from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DigitalProduct
from .serializers import DigitalProductSerializer, DigitalProductListSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import Http404
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from django.db.models import Q
from dPCategories.models import DPCategory 

class DigitalProductDetail(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
    def get_object(self, pk):
        try:
            return DigitalProduct.objects.get(pk=pk)
        except DigitalProduct.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk is not None:
            product = self.get_object(pk)
            serializer = DigitalProductSerializer(product, context={'request': request})
            return Response(serializer.data)
        else:
            all_products = DigitalProduct.objects.all()
            serializer = DigitalProductListSerializer(all_products, many=True, context={'request': request})
            return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = DigitalProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = DigitalProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DigitalProductCount(APIView):
    def get(self, request):
        # Filter products with releaseType == 1
        total_products = DigitalProduct.objects.filter(releaseType=1).count()
        return Response({"total_products": total_products})

class CustomPagination(PageNumberPagination):
    page_size = 10  # default page size
    page_size_query_param = 'page_size'
    max_page_size = 100


class DigitalProductListByCategory(generics.ListAPIView):
    serializer_class = DigitalProductListSerializer
    pagination_class = CustomPagination

    def get_descendant_category_ids(self, category_id):  # Add 'self'
        # Fetch the category and all its descendants
        descendants = []
        stack = [category_id]

        while stack:
            current = stack.pop()
            descendants.append(current)
            # Add children of the current category to the stack
            children = DPCategory.objects.filter(parent_id=current).values_list('id', flat=True)
            stack.extend(children)

        return descendants

    def get_queryset(self):
        queryset = DigitalProduct.objects.filter(releaseType=1)

        # Fetch categories and their descendants
        category_ids = self.request.query_params.get('category_ids')
        if category_ids:
            category_id_list = category_ids.split(',')
            all_category_ids = []
            for category_id in category_id_list:
                all_category_ids.extend(self.get_descendant_category_ids(int(category_id)))  
            queryset = queryset.filter(category__in=all_category_ids)

        # Apply price filters
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if min_price is not None:
            queryset = queryset.filter(price__gte=int(min_price))
        if max_price is not None:
            queryset = queryset.filter(price__lte=int(max_price))

        # Sorting logic
        sort_by = self.request.query_params.get('sort_by', '')  # Default to empty string
        valid_sort_fields = ['price', '-price', 'updated_at', '-updated_at']
        sort_fields = [field for field in sort_by.split(',') if field in valid_sort_fields]
        if sort_fields:
            queryset = queryset.order_by(*sort_fields)

        return queryset
