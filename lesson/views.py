from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from lesson.forms import LessonForm
from .models import Lesson
# Create your views here.
def lessons(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons': lessons
    }
    return render(request , 'lesson/lesson.html', context)

def create(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = LessonForm()
        return render(request, 'lesson/create.html', {'form': form})

def edit(request, pk):
    post = Lesson.objects.get(pk=pk)
    if request.method == "POST":
        form = LessonForm(request.POST, instance=post)
        if form.is_valid():
            post.save()
            return redirect('/room')
    else:
        form = LessonForm(instance=post)
    return render(request, 'room/edit.html', {'form': form})

def delete(request):
    data = json.loads(request.body)
    if request.method == "DELETE":
        if Lesson.delete_by_id(data['id']):
            return HttpResponse(status=200)
    return HttpResponse(status=400)