from django.contrib import admin
from .models import Jewellery, Category, ReviewRating

# Register your models here.


class JewelleryAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Jewellery)
admin.site.register(Category)
admin.site.register(ReviewRating)
