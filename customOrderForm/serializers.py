from rest_framework import serializers
from .models import CustomOrderForm  # Import Category model


class CustomOrderFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomOrderForm
        fields = (
            "id",
            "fullName",
            "companyName",
            "projectName",
            "mobile",
            "serviceId",
            "projectLocation",
            "investAmount", 
            "timeToCallId",
            "created_at"
        )

class CustomOrderFormSerializerList(serializers.ModelSerializer):

    class Meta:
        model = CustomOrderForm
        fields = (
            "id",
            "fullName",
            "companyName",
            "mobile",
            "serviceId",
            "created_at"
        )

