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
        request_data = json.loads(request.body)
        group = Group.get_by_group_name(request_data['name'])

        lectures = Lecture.get_by_group(group)
        response_data = [lecture.to_dict() for lecture in lectures]
        return JsonResponse(response_data, safe=False)
    else:
        return HttpResponse(status=404)


