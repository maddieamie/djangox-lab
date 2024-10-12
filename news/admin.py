from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import CustomModel



@admin.register(CustomModel)
class CustomModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'purchaser']  # Fields from CustomModel
    search_fields = ['title', 'description']  # Allows searching by title and description
    list_filter = ['purchaser']  # Filter by purchaser
    ordering = ['title']  # Default ordering by title
    prepopulated_fields = {'title': ('description',)}  # Auto-fill the title field based on the description (optional)
