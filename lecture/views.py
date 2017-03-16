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
        lesson = Lesson.get_by_lesson_name(data['lesson'])
        group = Group.get_by_group_name(data['group'])
        room = Room.get_by_room_name(data['room'])
        teacher = User.get_by_username(data['teacher'])
        number_by_schedule = data['number_by_schedule']
        date_time = data['date_time']
        lecture = Lecture(lesson=lesson, group=group, room=room, teacher=teacher,
                          number_by_schedule=number_by_schedule,
                          date_time=date_time)
        lecture.save()
        return HttpResponse(status=201)
    else:
        lessons = Lesson.get_all()
        groups = Group.get_all()
        rooms = Room.get_all()
        teachers = User.get_all()
        context = {
            'lessons': lessons,
            'groups': groups,
            'rooms': rooms,
            'teachers': teachers,
        }
        return render(request, 'lecture/create.html', context=context)
