from django.urls import path
from .views import (
    FooterInfoView,
    HeaderInfoView,
    AboutUsInfoView,
    ContactUsInfoView,
    PoliciesInfoView,MainBannerInfoView,HomeBannersInfoView
)

urlpatterns = [
    path('business-info/footer/', FooterInfoView.as_view(), name='footer-info'),
    path('business-info/header/', HeaderInfoView.as_view(), name='header-info'),
    path('business-info/about/', AboutUsInfoView.as_view(), name='about-us-info'),
    path('business-info/contact/', ContactUsInfoView.as_view(), name='contact-us-info'),
    path('business-info/policies/', PoliciesInfoView.as_view(), name='policies-info'),
    path('business-info/mainBanner/', MainBannerInfoView.as_view(), name='policies-info'),
    path('business-info/homeBanners/', HomeBannersInfoView.as_view(), name='policies-info'),
]
