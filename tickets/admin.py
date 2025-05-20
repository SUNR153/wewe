from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'quantity', 'bought_at')
    list_filter = ('event', 'user')
    date_hierarchy = 'bought_at'  # Фильтр по дате покупки