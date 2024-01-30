from django.urls import path
from room import consumers

websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]