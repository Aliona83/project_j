from django.urls import path
from . import views

app_name = 'jewelleries'  # This sets the app namespace to 'jewelleries'


urlpatterns = [
    path('', views.all_jewelleries, name='jewelleries'),
    path('jewelleries/<int:jewellery_id>', views.jewelleries_details, name='jewelleries_details'),
    path('add/', views.add_jewellery, name='add_jewellery'),
     path('edit/<int:jewellery_id>/', views.edit_jewellery, name='edit_jewellery'),
]