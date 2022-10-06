from .consumers import ChatConsumer

from django.urls import path, include, re_path

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            re_path(r'ws/chat/(?P<thread_id>\w+)/(?P<user_id>\w+)/$', ChatConsumer.as_asgi()),   
        ])
    ),
})
