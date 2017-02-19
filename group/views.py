import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Group


# Create your views here.

def groups(request):
    groups = Group.get_all()
    context = {
        'groups': groups
    }
    return render(request, 'group/group.html', context)


def create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        group = Group(**data)
        group.save()
        return HttpResponse(status=201)
    else:
        return render(request, 'group/create.html')


def edit(request, pk):
    post = Group.get(pk=pk)
    if request.method == "PUT":
        data = json.loads(request.body)
        group = Group(**data)
        group.save()
        return HttpResponse(status=200)
    else:
        context = {
            'post': post
        }
        return render(request, 'group/edit.html', context)


def delete(request):
    data = json.loads(request.body)
    if request.method == "DELETE":
        if Group.delete_by_id(data['id']):
            return HttpResponse(status=200, )
    return HttpResponse(status=400)


def show(request, pk):
    group = Group.get(pk=pk)
    # users = User.objects.filter(group=group)
    context = {
        'group': group,
        # 'users': users
    }
    return render(request, 'group/show_group.html', context)
