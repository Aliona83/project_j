from django.urls import path
from . import views

app_name = 'customjewellery'

urlpatterns = [
    path('', views.custom_jewellery_list, name='design_list'),
    path('create/', views.create_custom_jewellery, name='create_design'),
    path('<int:design_id>/', views.custom_jewellery_detail, name='design_detail'),
]