from django.http import HttpResponse
from django.shortcuts import render
from .models import Message
from .chat_bot import handle_message


def index(request):
	# Retrive messages from the database
	messages = Message.objects.order_by('-timestamp')
	return render(request, 'index.html', context={'messages': messages})

def new_message(request):
	# Retrieve the message from the POST request
	content = request.POST.get('content')
	print(content)

	# Create a new message objec
	message = Message(content=content, role='Human')

	# Save the message to the database
	message.save()

	# Retrive messages from the database
	messages = Message.objects.order_by('timestamp')

	# Interact with LLMs
	output = handle_message(content, history=messages)

	# Create a new message object
	message = Message(content=output, role='Bot')
	# Save the message to the database
	message.save()
	
	# Retrive messages from the database
	messages = Message.objects.order_by('timestamp')
	return render(request, 'index.html', context={'messages': messages})

def clear(request):
	Message.objects.all().delete()
	return render(request, 'index.html')
