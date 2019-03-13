from channels.routing import ProtocolTypeRouter, URLRouter
from foodprod.consumers import SocketConsumer
from django.urls import path
from foodprod.token_auth import TokenAuthMiddleware


application = ProtocolTypeRouter({
    'websocket': TokenAuthMiddleware(
        URLRouter([
            path('socket_consumer/', SocketConsumer)
        ]),
    ),
})