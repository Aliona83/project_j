from django.urls import path
from . import views

app_name = 'reviews'


urlpatterns = [
    path('jewelleries/<int:jewellery_id>/', views.add_review, name='add_review'),


]