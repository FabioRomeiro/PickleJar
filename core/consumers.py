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

    async def send_deleted_credential(self, event):
        await self.send(json.dumps(event))


class UserConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add('user', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('user', self.channel_name)

    async def send_logout(self, event):
        await self.send(json.dumps(event))

    async def send_updated_user(self, event):
        await self.send(json.dumps(event))
