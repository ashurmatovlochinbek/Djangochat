from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from room.models import Room, Message


@login_required
def rooms(request: HttpRequest):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request: HttpRequest, slug):
    room = Room.objects.get(slug = slug)
    messages = Message.objects.filter(room = room)[:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})

