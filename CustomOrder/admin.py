from django.contrib import admin
from .models import CustomJewelleryDesign

class CustomJewelleryDesignAdmin(admin.ModelAdmin):
    list_display = ('design_name', 'jewellery_type', 'metal_type', 'user_profile')
    list_filter = ('jewellery_type', 'metal_type')
    search_fields = ('design_name', 'user_profile__user__username', 'user_profile__user__email')
    
    def user_profile(self, obj):
        return obj.user_profile.user.username
    
    user_profile.short_description = 'User Profile'
    fieldsets = (
        ('Design Info', {
            'fields': ('design_name', 'jewellery_type', 'metal_type', 'stone_type', 'description', 'design_image', 'user_profile')
        }),
        ('Customer Details', {
            'fields': ('full_name', 'email', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county')
        }),
    )

admin.site.register(CustomJewelleryDesign, CustomJewelleryDesignAdmin)
