from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BusinessInfo
from .serializers import (
    FooterInfoSerializer,
    HeaderInfoSerializer,
    AboutUsInfoSerializer,
    ContactUsInfoSerializer,
    PoliciesInfoSerializer,HomeBannersSerializer,MainBannerSerializer
)
from django.http import Http404

class BusinessInfoBaseView(APIView):
    def get_object(self):
        try:
            return BusinessInfo.objects.first()  # Fetch the first and only record
        except BusinessInfo.DoesNotExist:
            raise Http404

# Footer Info View
class FooterInfoView(BusinessInfoBaseView):
    def get(self, request):
        business_info = self.get_object()
        serializer = FooterInfoSerializer(business_info)
        return Response(serializer.data)

# Header Info View
class HeaderInfoView(BusinessInfoBaseView):
    def get(self, request):
        business_info = self.get_object()
        serializer = HeaderInfoSerializer(business_info)
        return Response(serializer.data)

# About Us Info View
class AboutUsInfoView(BusinessInfoBaseView):
    def get(self, request):
        business_info = self.get_object()
        serializer = AboutUsInfoSerializer(business_info)
        return Response(serializer.data)

# Contact Us Info View
class ContactUsInfoView(BusinessInfoBaseView):
    def get(self, request):
        business_info = self.get_object()
        serializer = ContactUsInfoSerializer(business_info)
        return Response(serializer.data)

# Policies Info View
class PoliciesInfoView(BusinessInfoBaseView):
    def get(self, request):
        business_info = self.get_object()
        serializer = PoliciesInfoSerializer(business_info)
        return Response(serializer.data)

# MainBanner Info View
class MainBannerInfoView(BusinessInfoBaseView):
    def get(self, request):
        business_info = self.get_object()
        serializer = MainBannerSerializer(business_info)
        return Response(serializer.data)

# HomeBanners Info View
class HomeBannersInfoView(BusinessInfoBaseView):
    def get(self, request):
        business_info = self.get_object()
        serializer = HomeBannersSerializer(business_info)
        return Response(serializer.data)