from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/lobby/(?P<room_name>\w+)/$', consumers.lobbyConsumer.as_asgi()),
    re_path(r'ws/selection/(?P<room_name>\w+)/$', consumers.selectionConsumer.as_asgi()),
    re_path(r'ws/game/(?P<room_name>\w+)/$', consumers.gameConsumer.as_asgi()),
]
