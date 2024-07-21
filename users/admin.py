from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "email"]
    list_filter = ["username", "email"]
    search_fields = ["username", "email", "first_name", "last_name"]
