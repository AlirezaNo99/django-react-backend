from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register CustomUser with Django's UserAdmin
admin.site.register(CustomUser, UserAdmin)
