import json
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from group.models import Group
from lecture.models import Lecture
# Create your views here.
def schedule(request):
    groups = Group.objects.all()
    context = {
        'groups': groups
    }
    return render(request, 'schedule/schedule.html', context)

def group_schedule(request):
    if request.method == "POST":
        events = json.loads(request.body)
        group = Group.objects.get(name=events['name'])
        lecture = Lecture.objects.get(group=group)

        #date =''.join([x for x in 'T'.join(str(lecture.date_time).split())][:-6])
        #print(date)
        data = {
            'title': str(lecture.lesson),
            'start': lecture.date_time
        }
        return JsonResponse(data)
    else:
        return HttpResponse(status=404)


