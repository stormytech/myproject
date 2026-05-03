from django.shortcuts import render
from messaging.models import Message

def chat_screen(request):
    # This fetches all messages for the logged-in user
    messages = Message.objects.all().order_by('timestamp')
    return render(request, 'chat.html', {'messages': messages})