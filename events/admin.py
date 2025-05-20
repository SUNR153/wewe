from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'price', 'created_by')
    list_filter = ('date', 'created_by')
    search_fields = ('title', 'description')
    raw_id_fields = ('created_by',)  # Для удобного выбора пользователя

    # Автоматическое подставление создателя события
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Если событие создаётся впервые
            obj.created_by = request.user
        super().save_model(request, obj, form, change)