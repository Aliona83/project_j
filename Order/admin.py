from django.contrib import admin
from .models import CustomJewelleryDesign

@admin.register(CustomJewelleryDesign)
class CustomJewelleryDesignAdmin(admin.ModelAdmin):
    list_display = ('id', 'jewellery_type', 'metal_type', 'name', 'surname', 'created_at')
    list_filter = ('jewellery_type', 'metal_type', 'created_at')
    search_fields = ('name', 'surname', 'mobile_phone', 'address')
    ordering = ('-created_at',)
    fieldsets = (
        ('Jewellery Details', {
            'fields': ('jewellery_type', 'stone_type', 'metal_type', 'description', 'price')
        }),
        ('Contact Information', {
            'fields': ('name', 'surname', 'mobile_phone', 'address')
        }),
    )





