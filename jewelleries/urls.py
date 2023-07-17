from django.urls import path
from . import views 

app_name = 'jewelleries'  # This sets the app namespace to 'jewelleries'


urlpatterns = [
    path('', views.all_jewelleries, name='all_jewelleries')
]