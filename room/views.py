from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Room
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
import json
from django.db import IntegrityError


# Create your views here.

def validate_data_room(room):
    errors = {}
    if room['name']:
        if len(room['name']) > 50:
            errors['name'] = "Max input length is set to 50 characters."
    else:
        errors['name'] = "This field is required."
    if room['type']:
        if len(room['type']) > 10:
            errors['type'] = "Max input length is set to 50 characters."
    else:
        errors['type'] = "This field is required."
    if room['description']:
        if len(room['description']) > 240:
            errors['description'] = "Max input length is set to 240 characters."
    else:
        errors['description'] = "This field is required."
    try:
        if not room['size']:
            errors['size'] = "This field is required."
        else:
            size = int(room['size'])
            if size < 10:
                errors['size'] = 'Size must be greater than 10'
    except:
        errors['size'] = "Size must be integer."

    return errors if errors else None


def create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        errors = validate_data_room(data)
        if not errors:
            room = Room(**data)
            try:
                room.save()
                return HttpResponse(status=201)
            except IntegrityError:
                errors = {}
                errors["name"] = "Room with this name already exists."
                return HttpResponse(json.dumps(errors), status=400)
        else:
            return HttpResponse(json.dumps(errors), status=400)
    else:
        return render(request, 'room/create.html')


def room(request):
    rooms = Room.get_all()
    context = {
        'rooms': rooms
    }
    return render(request, 'room/room.html', context)


def edit(request, pk):
    post = Room.get_by_id(pk)
    if request.method == "PUT":
        data = json.loads(request.body)
        errors = validate_data_room(data)
        if not errors:
            room = Room(**data)
            #checking if we changed name
            if post.name == data["name"]:
                room.save()
                return HttpResponse(status=201)
            else:
                try:
                    room.save()
                    return HttpResponse(status=201)
                except IntegrityError:
                    errors = {}
                    errors["name"] = "Room with this name already exists."
                    return HttpResponse(json.dumps(errors), status=400)
        else:
            return HttpResponse(json.dumps(errors), status=400)
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
    room = Room.get_by_id(room_id)
    return render(request, 'room/show_room.html', {'room': room})


def home(request):
    return render(request, 'base.html')
