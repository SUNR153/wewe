from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('create/<int:event_id>/', views.order_create, name='order_create'),
]
