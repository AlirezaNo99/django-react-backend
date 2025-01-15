from rest_framework import serializers
from .models import DigitalProduct

class DigitalProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalProduct
        fields = (
            "id", "title", "category", "status", "keyWords", "summary", 
            "productLink", "mainPicAlt", "mainPic", "body_html", 
            "releaseType", "author_userName", "created_at", "updated_at","price"
        )

class DigitalProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalProduct
        fields = (
            "id", "title", "category", "status", "keyWords", "summary", 
            "releaseType", "author_userName", "created_at", "updated_at","price","thumbnail"
        )
