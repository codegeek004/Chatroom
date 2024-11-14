import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
	
	async def connect(self):
		self.room_name = self.scope['url_route']['kwargs']['room_name']
		self.room_group_name = 'chat%s' % self.room_name

		#join room group
		await channel_layer.group_add(self.room_group_name, self.channel_name)
		await self.accept()

	async def disconnect(self, close_node):
		#Leave from group
		await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

	#Receive message from the websocket
	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json["message"]

		# async_to_sync(self.channel_layer.group_send)(
		# 	self.room_group_name, {'type':'chat_message', 'message': message}
		# 	)

	#Recieve message from room group
	def chat_message(self, event):
		message = event["message"]

		#Send message to  websocket
		self.send(text_data=json.dumps({'message':message}))

		