import json
from channels.generic.websocket import AsyncWebsocketConsumer


class CredentialsConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add('credentials', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('credentials', self.channel_name)

    async def send_updated_credential(self, event):
        await self.send(json.dumps(event))
