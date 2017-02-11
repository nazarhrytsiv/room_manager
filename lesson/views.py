import json
from django.http import HttpResponse
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
        data = {}
        result = request.body.split('&')
        for i in result:
            data.update(dict([i.split("="), ]))
        lesson = Lesson(name=data['name'], place=data['place'], description=data['description'],
                        timeout=data['timeout'], )
        lesson.save()
        return redirect('/lesson')
    else:
        return render(request, 'lesson/create.html')


def edit(request, pk):
    post = Lesson.get(pk=pk)
    if request.method == "POST":
        data = {}
        result = request.body.split('&')
        for i in result:
            data.update(dict([i.split("="), ]))
        lesson = Lesson(name=data['name'], place=data['place'], description=data['description'],
                        timeout=data['timeout'], )
        lesson.id = pk
        lesson.save()
        return redirect('/lesson')
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
