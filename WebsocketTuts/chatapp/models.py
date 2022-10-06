from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages
# Create your models here.



class Thread(models.Model):
	user_from = models.ForeignKey(User, related_name='user_from', on_delete=models.CASCADE)
	user_to = models.ForeignKey(User, related_name='user_to', on_delete=models.CASCADE)
	is_opened_from = models.BooleanField(default=False)
	is_opened_to = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
    

class ChatMessage(models.Model):
	thread = models.ForeignKey(Thread, on_delete=models.SET_NULL, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
	message = models.TextField()
	is_read = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

