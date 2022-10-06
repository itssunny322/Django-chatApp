import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.conf import settings
 
from .models import ChatMessage, Thread
from .serializers import ChatMessageSerializer, ThreadSerializer

 
class ChatConsumer(WebsocketConsumer):
   def connect(self): 
       self.thread_id = self.scope['url_route']['kwargs']['thread_id']
       self.user_id = self.scope['url_route']['kwargs']['user_id']

       thread = Thread.objects.get(id=self.thread_id)
       if thread.user_from.id == int(self.user_id):
           thread.is_opened_from = True
           thread.save()
       elif thread.user_to.id == int(self.user_id):
           thread.is_opened_to = True
           thread.save()
       else :
           pass
      
 
       async_to_sync(self.channel_layer.group_add)(
           self.thread_id,
           self.channel_name
       )
       self.accept()
 
   def disconnect(self, close_code):
       self.thread_id = self.scope['url_route']['kwargs']['thread_id']
       self.user_id = self.scope['url_route']['kwargs']['user_id']
 
       thread = Thread.objects.get(id=self.thread_id)
       if thread.user_from.id == int(self.user_id):
           thread.is_opened_from = False
       elif thread.user_to.id == int(self.user_id):
           thread.is_opened_to = False
       thread.save()
 
   def receive(self, text_data):
       text_data_json = json.loads(text_data)
       message = text_data_json['msg_info']
       serializer_class = ChatMessageSerializer
 
       thread_id = self.scope['url_route']['kwargs']['thread_id']
       sender_id = self.scope['url_route']['kwargs']['user_id']
 
       thread = Thread.objects.get(id=thread_id)
 
       if int(sender_id) == thread.user_from.id:
           sender = thread.user_from
       else:
           sender = thread.user_to
 
       new_message = ChatMessage.objects.create(thread=thread, user=sender, message=message, is_read=True)
       new_message.save()
       serializer = serializer_class(new_message, many=False)
 
       if thread.user_from.id == sender.id:
           if thread.is_opened_to == False:
               new_message.is_read = False
               new_message.save()
       else:
           if thread.is_opened_from == False:
               new_message.is_read = False
               new_message.save()
 
 
       async_to_sync(self.channel_layer.group_send)(
           self.thread_id,
           {
               'type': 'chat_message',
               'msg_info': serializer.data
           }
       )
 
 
   def chat_message(self, event):
       message = event['msg_info']
       self.send(text_data=json.dumps({
           'msg_info': message
       }))
