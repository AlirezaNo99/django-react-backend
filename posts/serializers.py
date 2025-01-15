from rest_framework import serializers
from .models import Post, Category  # Import Category model


class PostSerializer(serializers.ModelSerializer):
    # Define category as a PrimaryKeyRelatedField to only accept the category ID
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "category",
            "status",
            "keyWords",
            "summary",
            "mainPic",
            "body_html",
            "releaseType",
            "author_userName",
            "mainPicAlt",
            "created_at",  # Include the new fields
            "updated_at",
         
        )

class PostListSerializer(serializers.ModelSerializer):
    # Define category as a PrimaryKeyRelatedField to only accept the category ID
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "category",
            "status",
            "keyWords",
            "summary",
            "thumbnail",
            "releaseType",
            "author_userName",
            "mainPicAlt",
            "created_at",  # Include the new fields
            "updated_at",
            "thumbnail"
        )

    def create(self, validated_data):
        # Create the post with the validated data directly
        return Post.objects.create(**validated_data)
