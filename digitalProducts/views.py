from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DigitalProduct
from .serializers import DigitalProductSerializer, DigitalProductListSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import Http404
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics

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
        total_products = DigitalProduct.objects.count()
        return Response({"total_products": total_products})

class CustomPagination(PageNumberPagination):
    page_size = 10  # default page size
    page_size_query_param = 'page_size'
    max_page_size = 100

class DigitalProductListByCategory(generics.ListAPIView):
    serializer_class = DigitalProductListSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return DigitalProduct.objects.filter(category=category_id)