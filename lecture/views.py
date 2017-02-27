from django.shortcuts import render
from .models import Lecture

# Create your views here.
def lectures(request):
    lectures = Lecture.get_all()
    context = {
        'lectures': lectures,
    }
    return render(request, 'lecture/lecture.html', context)