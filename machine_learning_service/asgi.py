"""
ASGI config for machine_learning_service project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from chatapp.middleware import websockets

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'machine_learning_service.settings')

django_application = get_asgi_application()

application = get_asgi_application()
application = websockets(application)

# async def websocket_application(scope, receive, send):
#     while True:
#         event = await receive()
#
#         if event['type'] == 'websocket.connect':
#             await send({
#                 'type': 'websocket.accept'
#             })
#
#         if event['type'] == 'websocket.disconnect':
#             break
#
#         if event['type'] == 'websocket.receive':
#             if event['text'] == 'ping':
#                 await send({
#                     'type': 'websocket.send',
#                     'text': 'pong!'
#                 })

# async def application(scope, receive, send):
#     if scope['type'] == 'http' or scope['type'] == 'https':
#         await django_application(scope, receive, send)
#     elif scope['type'] == 'websocket':
#         print("received websocket request!")
#
#         await websocket_application(scope, receive, send)
#     else:
#         raise NotImplementedError(f"Unknown scope type")

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     # Just HTTP for now. (We can add other protocols later.)
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             chatapp.routing.websocket_urlpatterns
#         )
#     ),
# })
