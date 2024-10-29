from rest_framework import serializers
from .models import DPCategory

class DPCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DPCategory
        fields = ("id", "name", "parent")
