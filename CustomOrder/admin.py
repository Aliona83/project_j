from django.contrib import admin
from .models import CustomJewelleryDesign, CustomerDetails

@admin.register(CustomJewelleryDesign)
class CustomJewelleryDesignAdmin(admin.ModelAdmin):
    list_display = ('design_name', 'jewellery_type', 'metal_type', 'stone_type', 'user')
    list_filter = ('jewellery_type', 'metal_type', 'stone_type', 'user')
    search_fields = ('design_name', 'description')
    readonly_fields = ('user',)  # Make 'user' field read-only
    # Add any other customization options you want
    
@admin.register(CustomerDetails)
class CustomerDetailsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'country')
    list_filter = ('country',)
    search_fields = ('full_name', 'email', 'phone_number')
    # Add any other customization options you want

# You can also customize the admin site header and title
admin.site.site_header = "Your Jewelry Shop Admin"
admin.site.site_title = "Your Jewelry Shop Admin Panel"

