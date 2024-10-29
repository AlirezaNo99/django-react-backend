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
            "email",
            "postalCode",
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
            "address",
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
