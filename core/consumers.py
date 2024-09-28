# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SomeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        #connect includes user authentication etc.

        # after verifying user Accept the connection

        await self.accept()

    async def disconnect(self, close_code):
        # Disconnect logic
        pass

    async def receive(self, text_data):
        # Logic for handling received messages
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message back to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def custom_method(self, event):
        custom_update_data = event['custom_update']  #

        await self.send(text_data=json.dumps({
            'custom_update_data': custom_update_data,
        }))

