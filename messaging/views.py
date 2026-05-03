from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User, Message

def register(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']

        User.objects.create_user(
            username=phone,
            phone_number=phone,
            password=password
        )
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']

        user = authenticate(request, username=phone, password=password)

        if user:
            login(request, user)
            return redirect('chat')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def chat(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat.html', {'users': users})


def room(request, username):
    receiver = User.objects.get(username=username)
    messages = Message.objects.filter(
        sender=request.user, receiver=receiver
    ) | Message.objects.filter(
        sender=receiver, receiver=request.user
    )

    messages = messages.order_by('timestamp')

    return render(request, 'room.html', {
        'receiver': receiver,
        'messages': messages
    })