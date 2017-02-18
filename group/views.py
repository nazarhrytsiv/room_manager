import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Group


# Create your views here.

def groups(request):
    groups = Group.get_all()
    context = {
        'groups': groups
    }
    return render(request, 'group/group.html', context)


def create(request):
    print  "post"
    if request.method == "POST":
        print 11111111
        data = json.loads(request.body)
        group = Group(**data)
        group.save()
        respons = {"a": 1, "b": 2}
        print respons
        return JsonResponse(data=respons, status=201)
        # return redirect('/group')
    else:
        return render(request, 'group/create.html')


def edit(request, pk):
    post = Group.get(pk=pk)
    if request.method == "POST":
        data = {}
        result = request.body.split('&')
        for i in result:
            data.update(dict([i.split("="), ]))
        group = Group(name=data['name'], description=data['description'])
        group.id = pk
        group.save()
        return redirect('/group')
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
