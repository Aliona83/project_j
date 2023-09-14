from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('delete_order/<str:order_number>/', views.delete_order, name='delete_order'),
]
