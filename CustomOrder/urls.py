from django.urls import path
from . import views

app_name = 'CustomOrder'

urlpatterns = [
    path('', views.create_custom_jewellery, name='design_jewellery'),
]


