from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser  # Add this import
from rest_framework import status
from .models import Post
from .serializers import PostSerializer, PostListSerializer
from django.http import Http404
from rest_framework import generics
from categories.models import Category 


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
        total_posts = Post.objects.filter(releaseType=1).count()
        return Response({"total_posts": total_posts})

class CustomPagination(PageNumberPagination):
    page_size = 10  # default page size
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostListByCategory(generics.ListAPIView):
    serializer_class = PostListSerializer
    pagination_class = CustomPagination
    def get_descendant_category_ids(self, category_id):  # Add 'self'
        # Fetch the category and all its descendants
        descendants = []
        stack = [category_id]

        while stack:
            current = stack.pop()
            descendants.append(current)
            # Add children of the current category to the stack
            children = Category.objects.filter(parent_id=current).values_list('id', flat=True)
            stack.extend(children)

        return descendants

    def get_queryset(self):
        queryset = Post.objects.filter(releaseType=1)

        # Filter by multiple category IDs
        category_ids = self.request.query_params.get('category_ids')
        if category_ids:
            category_id_list = category_ids.split(',')
            all_category_ids = []
            for category_id in category_id_list:
                all_category_ids.extend(self.get_descendant_category_ids(int(category_id)))
            queryset = queryset.filter(category__in=all_category_ids)

        # Sorting
        sort_by = self.request.query_params.get('sort_by')
        if sort_by:
            sort_fields = sort_by.split(',')
            valid_sort_fields = [field for field in sort_fields if field in [ 'updated_at', '-updated_at']]
            if valid_sort_fields:
                queryset = queryset.order_by(*valid_sort_fields)

        return queryset