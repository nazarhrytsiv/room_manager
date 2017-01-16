from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response

from .models import Room
from .forms import RoomForm
from django.shortcuts import redirect

# Create your views here.

def room(request):
    rooms = Room.objects.all()
    context = {
        'rooms' : rooms
    }
    return render(request, 'room/room.html' , context)

def create(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('post_detail', pk=create.id)
    else:
        form = RoomForm()
    return render(request, 'room/create.html', {'form': form})

def edit(request, pk):
    post = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=post)
        if form.is_valid():
            post.save()
            return redirect('/')
    else:
        form = RoomForm(instance=post)
    return render(request, 'room/edit.html', {'form': form})


def delete(request, pk):
    post = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=post)
        if form.is_valid():
            post.delete()
            return redirect('/')
    else:
        form = RoomForm(instance=post)
    return render(request, 'room/delete.html', {'form': form})


def show_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'room/show_room.html', {'room': room})


def home(request):
    return render(request, 'base.html')