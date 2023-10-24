from django.urls import path
from . import views

app_name = 'whishlist' 

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path(
        'add_to_wishlist/<jewellery_id>',
        views.add_to_wishlist,
        name='add_to_wishlist'),
    path(
        'remove_from_wishlist/<jewellery_id>',
        views.remove_from_wishlist,
        name='remove_from_wishlist'),
]