import json
from django.http import HttpResponse
from django.utils.http import urlencode
from django.shortcuts import render, redirect
from .models import Lecture
from lesson.models import Lesson
from group.models import Group
from room.models import Room
from user.models import User


def validate_data_lecture(lecture):
    errors = {}
    try:
        if not lecture['number_by_schedule']:
            errors['number_by_schedule'] = "This field is required."
        else:
            number_by_schedule = int(lecture['number_by_schedule'])
            if number_by_schedule != int(number_by_schedule):
                errors['number_by_schedule'] = "Number by schedule cannot be float."
            if number_by_schedule > 7:
                errors['number_by_schedule'] = 'Number by schedule must be less than 7.'
            elif number_by_schedule < 1:
                errors['number_by_schedule'] = 'Number by schedule must be greater than or equals to 1.'
    except:
        errors['number_by_schedule'] = "Number by schedule must be integer."
    return errors if errors else None


def lectures(request):
    lectures = Lecture.get_all()
    context = {
        'lectures': lectures,
    }
    return render(request, 'lecture/lecture.html', context)


def create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        errors = validate_data_lecture(data)
        if not errors:
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
            return HttpResponse(json.dumps(errors), status=400)
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


def edit(request, pk):
    post = Lecture.get_by_id(pk=pk)
    if request.method == "PUT":
        data = json.loads(request.body)
        errors = validate_data_lecture(data)
        if not errors:
            lesson = Lesson.get_by_lesson_name(data['lesson'])
            group = Group.get_by_group_name(data['group'])
            room = Room.get_by_room_name(data['room'])
            teacher = User.get_by_username(data['teacher'])
            number_by_schedule = data['number_by_schedule']
            date_time = data['date_time']
            lecture = Lecture(pk=pk, lesson=lesson, group=group, room=room, teacher=teacher,
                              number_by_schedule=number_by_schedule,
                              date_time=date_time)
            lecture.save()
            return HttpResponse(status=201)
        else:
            return HttpResponse(json.dumps(errors), status=400)
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
            'post': post,
        }
        return render(request, 'lecture/edit.html', context)


def delete(request):
    data = json.loads(request.body)
    if request.method == "DELETE":
        if Lecture.delete_by_id(data['id']):
            return HttpResponse(status=200)
    return HttpResponse(status=400)

