from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response

from .models import Room
from .forms import RoomForm
from django.shortcuts import redirect
from django.http import HttpResponse
import json



# Create your views here.

def room(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'room/room.html', context)


def create(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/room')
    else:
        form = RoomForm()
    return render(request, 'room/create.html', {'form': form})


def edit(request, pk):
    post = Room.objects.get(pk=pk)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=post)
        if form.is_valid():
            post.save()
            return redirect('/room')
    else:
        form = RoomForm(instance=post)
    return render(request, 'room/edit.html', {'form': form})


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
