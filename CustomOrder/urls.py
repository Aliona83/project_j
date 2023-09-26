from django.urls import path
from . import views

app_name = 'CustomOrder'

urlpatterns = [
    path('', views.create_custom_jewellery, name='design_jewellery'),
    path('submitted_success/',
         views.submitted_success, name='submitted_success'),
    path('submitted_forms/',
         views.view_submitted_forms, name='view_submitted_forms'),
]
