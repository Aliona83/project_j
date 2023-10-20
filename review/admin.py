from django.contrib import admin
from .models import Review

# @admin.register(Review)
# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ['id', 'jewellery', 'rate', 'comment', 'user', 'created_at', ]
#     readonly_fields = ['user', 'created_at', 'rate', ]

#     class Meta:
#         verbose_name_plural = 'Review'

admin.site.register(Review)