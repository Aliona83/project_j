from django.contrib import admin
from .models import CustomJewelleryDesign

@admin.register(CustomJewelleryDesign)
class CustomJewelleryDesignAdmin(admin.ModelAdmin):
    list_display = ('design_name', 'jewellery_type', 'metal_type', 'user_display')
    list_filter = ('jewellery_type', 'metal_type')
    search_fields = ('design_name', 'user__username', 'user__email')
    
    def user_display(self, obj):
        return obj.user.username

    user_display.short_description = 'User'  # Set a custom column header

    fieldsets = (
        ('Design Info', {
            'fields': ('design_name', 'jewellery_type', 'metal_type', 'stone_type', 'description', 'design_image', 'user')
        }),
        ('Customer Details', {
            'fields': ('full_name', 'email', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county')
        }),
    )


