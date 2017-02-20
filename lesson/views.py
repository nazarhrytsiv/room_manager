import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Lesson


# Create your views here.
def lessons(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons': lessons
    }
    return render(request, 'lesson/lesson.html', context)


def create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        lesson = Lesson(**data)
        lesson.save()
        return HttpResponse(status=201)
    else:
        return render(request, 'lesson/create.html')


def edit(request, pk):
    post = Lesson.get(pk=pk)
    if request.method == "PUT":
        data = json.loads(request.body)
        lesson = Lesson(**data)
        lesson.save()
        return HttpResponse(status=200)
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
