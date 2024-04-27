from django.contrib import admin
from django.urls import path, include

from ride import routing

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/accounts/', include('api.v1.accounts.urls', namespace='api_v1_accounts')),
    path('api/v1/ride/', include('api.v1.ride.urls', namespace='api_v1_ride')),

    path('ride_tracking/', include(routing.websocket_urlpatterns)),
]
