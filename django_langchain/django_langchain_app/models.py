from django.db import models

class Message(models.Model):
	content = models.TextField()
	role = models.CharField(max_length=10) # Human or Bot
	timestamp = models.DateTimeField(auto_now_add=True)