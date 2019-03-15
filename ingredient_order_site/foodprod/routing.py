from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/socket_consumer/', consumers.SocketConsumer),
]