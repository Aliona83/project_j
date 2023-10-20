from django.urls import path
from . import views

app_name = 'review'


urlpatterns = [
    path('jewelleries/<int:jewellery_id>/review/', views.add_review, name='submit_review'),


]