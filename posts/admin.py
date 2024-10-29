from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "status",
        "keyWords",
        "summary",
        "mainPic",
        "body_html",
        "releaseType",
        "author_userName",
        "created_at",  # Include the new fields
        "updated_at",
    )


admin.site.register(Post, PostAdmin)
