from django.contrib import admin
from .models import BusinessInfo


class BusinessInfoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "logoLight",
        "logoDark",
        "aboutUs",
        "aboutUsSummary",
        "aboutUsImage",
        "email",
        "tel",
        "tel2",
        "postalCode",
        "address",
        "contactUsImage",
        "policies",
        "policiesImage",
        "created_at",  
        "updated_at",
        "mainBanner",
        "mainBannerText",
        "mainBannerLink",
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
        "Telegram",
        "Linkedin",
        "Instagram",
        "address2",
    )


admin.site.register(BusinessInfo, BusinessInfoAdmin)
