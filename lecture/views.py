import json
from django.http import HttpResponse
from django.utils.http import urlencode
from django.shortcuts import render, redirect
from .models import Lecture
from lesson.models import Lesson
from group.models import Group
from room.models import Room
from user.models import User

# Create your views here.
def lectures(request):
    lectures = Lecture.get_all()
    context = {
        'lectures': lectures,
    }
    return render(request, 'lecture/lecture.html', context)

def create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        lesson = Lesson.objects.get(name=data['lesson'])
        group = Group.objects.get(name=data['group'])
        room = Room.objects.get(name=data['room'])
        teacher = User.objects.get(name=data['teacher'])
        lecture = Lecture(lesson=lesson,group=group,room=room,teacher=teacher)
        lecture.save()
        return HttpResponse(status=201)
    else:
        lessons = Lesson.objects.all()
        groups = Group.objects.all()
        rooms = Room.objects.all()
        teachers = User.objects.all()
        context = {
            'lessons':lessons,
            'groups': groups,
            'rooms': rooms,
            'teachers': teachers,
        }
        return render(request, 'lecture/create.html', context=context)
