import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Lesson


def validate_data_lesson(lesson):
    errors = {}
    if lesson['name']:
        if len(lesson['name']) > 50:
            errors['name'] = "Max input length is set to 50 characters."
    else:
        errors['name'] = "This field is required."
    if lesson['description']:
        if len(lesson['description']) > 240:
            errors['description'] = "Max input length is set to 240 characters."
    else:
        errors['description'] = "This field is required."
    if lesson['place']:
        if len(lesson['place']) > 15:
            errors['place'] = "Max input length is set to 15 characters."
    else:
        errors['place'] = "This field is required."
    return errors if errors else None



# Create your views here.
def lessons(request):
    lessons = Lesson.get_all()
    context = {
        'lessons': lessons
    }
    return render(request, 'lesson/lesson.html', context)


def create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        errors = validate_data_lesson(data)
        if not errors:
            lesson = Lesson(**data)
            lesson.save()
            return HttpResponse(status=201)
        else:
            return HttpResponse(json.dumps(errors),status=400)
    else:
        return render(request, 'lesson/create.html')


def edit(request, pk):
    post = Lesson.get_by_id(pk)
    if request.method == "PUT":
        data = json.loads(request.body)
        errors = validate_data_lesson(data)
        if not errors:
            lesson = Lesson(**data)
            lesson.save()
            return HttpResponse(status=201)
        else:
            return HttpResponse(json.dumps(errors), status=400)
    else:
        context = {
            'post': post
        }
        return render(request, 'lesson/edit.html', context)


def delete(request):
    data = json.loads(request.body)
    if request.method == "DELETE":
        if Lesson.delete_by_id(data['id']):
            return HttpResponse(status=200)
    return HttpResponse(status=400)
