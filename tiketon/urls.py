from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', include('events.urls', namespace='events')),
    path('venues/', include('venues.urls', namespace='venues')),
    path('orders/', include('orders.urls', namespace='orders')),
]
