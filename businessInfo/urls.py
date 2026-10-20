from django.urls import path

from .views import (
    FooterInfoView,
    HeaderInfoView,
    AboutUsInfoView,
    ContactUsInfoView,
    PoliciesInfoView,
    MainBannerInfoView,
    PromoInfoView,
    HomeBannersInfoView,
    BusinessInfoUpdateView,
    AllBusinessInfoView,
    CertificateListCreateView,
    CertificateDetailView,
)


urlpatterns = [

    path(
        'business-info/footer/',
        FooterInfoView.as_view(),
        name='footer-info'
    ),

    path(
        'business-info/header/',
        HeaderInfoView.as_view(),
        name='header-info'
    ),

    path(
        'business-info/about/',
        AboutUsInfoView.as_view(),
        name='about-us-info'
    ),

    path(
        'business-info/contact/',
        ContactUsInfoView.as_view(),
        name='contact-us-info'
    ),

    path(
        'business-info/policies/',
        PoliciesInfoView.as_view(),
        name='policies-info'
    ),

    path(
        'business-info/mainBanner/',
        MainBannerInfoView.as_view(),
        name='main-banner'
    ),

    path(
        'business-info/promo/',
        PromoInfoView.as_view(),
        name='promo-info'
    ),

    path(
        'business-info/homeBanners/',
        HomeBannersInfoView.as_view(),
        name='home-banners'
    ),

    path(
        'business-info/update/',
        BusinessInfoUpdateView.as_view(),
        name='business-info-update'
    ),

    path(
        'business-info/all-info/',
        AllBusinessInfoView.as_view(),
        name='all-business-info'
    ),

    # Certificates
    path(
        'business-info/certificates/',
        CertificateListCreateView.as_view(),
        name='certificate-list-create'
    ),

    path(
        'business-info/certificates/<int:pk>/',
        CertificateDetailView.as_view(),
        name='certificate-detail'
    ),

]