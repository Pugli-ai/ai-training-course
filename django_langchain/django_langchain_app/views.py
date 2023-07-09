from django.http import HttpResponse
from django.shortcuts import render
from .models import Message

def index(request):
	# Retrive messages from the database
	messages = Message.objects.order_by('-timestamp')
	return render(request, 'index.html', context={'messages': messages})