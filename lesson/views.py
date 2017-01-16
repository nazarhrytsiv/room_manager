from django.shortcuts import render
from .models import Lesson
# Create your views here.
def lessons(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons': lessons
    }
    return render(request , 'lesson/lesson.html', context)