from rest_framework import serializers
from .models import BusinessInfo 


class FooterInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusinessInfo
        fields = (
            "id",
            "aboutUsSummary",
            "logoDark",
            "logoLight",
            "address",
            "tel",
            "tel2",
            "email",
            "postalCode",
            "Telegram",
            "Linkedin",
            "Instagram",
            "address2",

        )

class HeaderInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusinessInfo
        fields = (
            "id",
            "logoDark",
            "logoLight",
        )
class AboutUsInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusinessInfo
        fields = (
            "id",
            "name",
            "aboutUsImage",
            "aboutUs",
        )

class ContactUsInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusinessInfo
        fields = (
            "id",
            "tel",
            "tel2",
            "address",
            "address2",
            "email",
            "contactUsImage",
            "postalCode",
        )


class MainBannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusinessInfo
        fields = (
            "id",
            "mainBanner",
            "mainBannerText",
            "mainBannerLink",
        )

class HomeBannersSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusinessInfo
        fields = (
            "id",
            "Banner1",
            "Banner1Text",
            "Banner1Link",
            "Banner2",
            "Banner2Text",
            "Banner2Link",
            "Banner3",
            "Banner3Text",
            "Banner3Link",
            "Banner4",
            "Banner4Text",
            "Banner4Link",
            "Banner5",
            "Banner5Text",
            "Banner5Link",

        )

class PoliciesInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusinessInfo
        fields = (
            "id",
            "policies",
            "policiesImage",
           
        )

    def create(self, validated_data):
        # Create the post with the validated data directly
        return BusinessInfo.objects.create(**validated_data)

class BusinessInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessInfo
        fields = "__all__"

    def update(self, instance, validated_data):
        # Explicitly handle each image field
        image_fields = [
            "logoDark", "logoLight", "aboutUsImage", "contactUsImage", "policiesImage",
            "mainBanner", "Banner1", "Banner2", "Banner3", "Banner4", "Banner5"
        ]
        for field in image_fields:
            if field in validated_data:
                # Delete the old file if a new file is provided
                old_file = getattr(instance, field)
                new_file = validated_data[field]
                if old_file and old_file != new_file and hasattr(old_file, "path"):
                    old_file.delete(save=False)
        
        return super().update(instance, validated_data)

class AllBusinessInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessInfo
        fields = (
            "__all__"
        )