from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('events/', include('events.urls')),
    path('tickets/', include('tickets.urls')),
    path('', include('events.urls')),
]
