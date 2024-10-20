from django.contrib import admin

from .models import Homepage


@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "institution", "profile_image", "email")
