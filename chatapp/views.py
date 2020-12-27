from django.views.generic.base import TemplateView
from django.shortcuts import render

from websocket import WebSocket
from .consumers import ChatConsumer

import logging


class IndexView(TemplateView):
    template_name = "index.html"


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })


async def websocket_view(socket: WebSocket, room_name):
    c = ChatConsumer(room_name=room_name)

    while True:
        event = await socket.receive()

        if event['type'] == 'websocket.connect':
            await c.connect()

        if event['type'] == 'websocket.disconnect':
            await c.disconnect(room_name)

        if event['type'] == 'websocket.receive':
            await c.receive(event)

