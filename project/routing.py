from django.urls import re_path
from core.consumers import *

websocket_urlpatterns = [
    re_path(r'ws/dumy/$', ) #consumers.SomeConsumer.as_asgi()
]
