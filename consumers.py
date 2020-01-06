from channels.generic.websocket import AsyncWebsocketConsumer
import json


class EnablePublishConsumer(AsyncWebsocketConsumer):
    """
    Websocket consumer to notify frontend if the page publishing finished
    """

    room_name = 'cms'

    async def connect(self):
        """
        Accept a websocket connection
        """

        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, close_code):
        """
        Close a websocket connnection
        """

        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def receive(self, bytes_data):
        """
        Receive data from CMS backend when the page is published
        """

        published = bytes_data.decode('utf-8')

        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'enable_button',
                'published': published,
            }
        )

    async def enable_button(self, event):
        """
        Dispatch data to frontend to enable the publish button
        """

        published = event['published']

        await self.send(text_data=json.dumps({
                'published': published,
        }))
