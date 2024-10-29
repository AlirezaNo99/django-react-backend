from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser  # Add this import
from rest_framework import status
from .models import Post
from .serializers import PostSerializer, PostListSerializer
from django.http import Http404


class PostDetail(APIView):
    parser_classes = (MultiPartParser, FormParser)  # Add this to handle file uploads
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk is not None:
            post = self.get_object(pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        else:
            # Extract query parameters for filtering
            filters = {}
            id = request.query_params.get("id")
            title = request.query_params.get("title")
            category = request.query_params.get("category")
            status = request.query_params.get("status")
            release_type = request.query_params.get("releaseType")
            author_username = request.query_params.get("author_userName")

            # Apply filters if present
            if id:
                filters["id"] = id
            if title:
                filters["title__icontains"] = title  # Use __icontains for partial matching
            if category:
                filters["category"] = category
            if status:
                filters["status"] = status
            if release_type:
                filters["releaseType"] = release_type
            if author_username:
                filters["author_userName__icontains"] = author_username

            # Filter the posts based on the constructed filters
            filtered_posts = Post.objects.filter(**filters)

            # Handle pagination
            paginator = PageNumberPagination()
            page = paginator.paginate_queryset(filtered_posts, request)
            if page is not None:
                serializer = PostSerializer(page, many=True)
                return paginator.get_paginated_response(serializer.data)

            serializer = PostSerializer(filtered_posts, many=True)
            return Response(serializer.data)

    def post(self, request, pk=None):
        # Use the MultiPartParser to handle the image file upload
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data, partial=True)  # partial=True for updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostCount(APIView):
    def get(self, request):
        total_posts = Post.objects.count()
        return Response({"total_posts": total_posts})
