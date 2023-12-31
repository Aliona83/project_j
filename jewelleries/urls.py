from django.urls import path
from . import views

app_name = 'jewelleries'  # This sets the app namespace to 'jewelleries'


urlpatterns = [
    path('', views.all_jewelleries, name='jewelleries'),
    path(
        'jewelleries/<int:jewellery_id>',
        views.jewelleries_details, name='jewelleries_details'),
    path('add/', views.add_jewellery, name='add_jewellery'),
    path(
        'edit/<int:jewellery_id>/',
        views.edit_jewellery, name='edit_jewellery'),
    path(
        'delete/<int:jewellery_id>/',
        views.delete_jewellery, name='delete_jewellery'),
    path(
        'submit_review/<int:jewellery_id>/',
        views.submit_review, name='submit_review'),
]
