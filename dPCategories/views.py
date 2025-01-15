from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import DPCategory
from .serializers import DPCategorySerializer
import logging

class DPCategoryDetail(APIView):
    def get_object(self, pk):
        try:
            return DPCategory.objects.get(pk=pk)
        except DPCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk is not None:
            category = self.get_object(pk)
            serializer = DPCategorySerializer(category)
            return Response(serializer.data)
        else:
            categories = DPCategory.objects.all()
            serializer = DPCategorySerializer(categories, many=True)
            return Response(serializer.data)
            
    def post(self, request):
        # Log request data for debugging
        logger = logging.getLogger(__name__)
        logger.info(f"Received data: {request.data}")
        
        data = request.data.copy()

        # Handle 'null' string case explicitly
        if data.get('parent') in [None, 'null', '']:
            data['parent'] = None

        serializer = DPCategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk):
        category = self.get_object(pk)
        data = request.data.copy()

        # Handle null or empty parent field
        if 'parent' not in data or data['parent'] in [None, '', 'null']:
            data['parent'] = None

        serializer = DPCategorySerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class DPCategoryCount(APIView):
    def get(self, request):
        total_categories = DPCategory.objects.count()
        return Response({"total_categories": total_categories})