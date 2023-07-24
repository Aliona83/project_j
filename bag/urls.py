from django.contrib import admin
from django.urls import path
from . import views 

app_name = 'view_bag' # This sets the app namespace to 'view_bag'

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
     path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
]
  