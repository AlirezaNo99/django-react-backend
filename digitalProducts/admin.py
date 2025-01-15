from django.contrib import admin
from .models import DigitalProduct


class digitalProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "keyWords",
        "summary",
        "mainPic",
        "body_html",
        "releaseType",
        "author_userName",
        "price"
    )


admin.site.register(DigitalProduct, digitalProductAdmin)
