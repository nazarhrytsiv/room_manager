from django.shortcuts import render
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from group.forms import GroupForm
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
        print request.body
        data = {}
        result = request.body.split('&')
        for i in result:
            data.update(dict([i.split("="), ]))
        group = Group(name=data['name'],description=data['description'])
        print group
        group.save()
        return HttpResponse(status=200)
    else:
        return render(request, 'group/create.html')
# def create(request):
#     if request.method == 'POST':
#         print 1
#         form = GroupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/group')
#     else:
#         print 0
#         form = GroupForm()
#         return render(request, 'group/create.html', {'form': form})

def edit(request, pk):
    post = Group.get(pk)
    if request.method == "POST":
        form = GroupForm(request.POST, instance=post)
        if form.is_valid():
            post.save()
            return redirect('/group')
    else:
        form = GroupForm(instance=post)
    return render(request, 'group/edit.html', {'form': form})


def delete(request):
    data = json.loads(request.body)
    if request.method == "DELETE":
        if Group.delete_by_id(data['id']):
            return HttpResponse(status=200, )
    return HttpResponse(status=400)


def show(request, pk):
    group = get_object_or_404(Group, pk=pk)
    # users = User.objects.filter(group=group)
    context = {
        'group': group,
        # 'users': users
    }
    return render(request, 'group/show_group.html', context)