from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    path('buy/<int:event_id>/', views.buy_ticket, name='buy_ticket'),
    path('', views.ticket_list, name='ticket_list'),
    path('<int:pk>/', views.ticket_detail, name='ticket_detail'),
]
