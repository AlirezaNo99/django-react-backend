from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from digitalProducts.models import DigitalProduct
from posts.models import Post
from digitalProducts.serializers import DigitalProductListSerializer
from posts.serializers import PostListSerializer

class GlobalSearchView(APIView):
    def get(self, request):
        query = request.GET.get('q', '')

        if not query:
            return Response({"error": "No search query provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Search in DigitalProduct titles
        digital_products = DigitalProduct.objects.filter(title__icontains=query)

        # Search in Post titles
        posts = Post.objects.filter(title__icontains=query)

        return Response({
            "digital_products": DigitalProductListSerializer(digital_products, many=True).data,
            "posts": PostListSerializer(posts, many=True).data,
        }, status=status.HTTP_200_OK)