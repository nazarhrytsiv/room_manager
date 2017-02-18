from django.shortcuts import render, get_object_or_404
from .models import Room
from django.shortcuts import redirect
from django.http import HttpResponse
import json


# Create your views here.

def room(request):
    rooms = Room.get_all()
    context = {
        'rooms': rooms
    }
    return render(request, 'room/room.html', context)


def create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        room = Room(**data)
        room.save()
        return HttpResponse(status=201)
    else:
        return render(request, 'room/create.html')


def edit(request, pk):
    post = Room.get(pk=pk)
    if request.method == "POST":
        data = {}
        result = request.body.split('&')
        for i in result:
            data.update(dict([i.split("="), ]))
        room = Room(name=data['name'], type=data['type'], description=data['description'], size=data['size'], )
        room.id = pk
        room.save()
        return redirect('/room')
    else:
        context = {
            'post': post
        }
        return render(request, 'room/edit.html', context)


def delete(request):
    data = json.loads(request.body)
    if request.method == "DELETE":
        if Room.delete_by_id(data['id']):
            return HttpResponse(status=200)
    return HttpResponse(status=400)


def show_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'room/show_room.html', {'room': room})


def home(request):
    return render(request, 'base.html')
