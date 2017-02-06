import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from user.forms import UserForm, GroupForm
from .models import User
from .models import Group
# Create your views here.
def users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request , 'user/user.html', context)

def create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserForm()
        return render(request, 'lesson/create.html', {'form': form})

def edit(request, pk):
    post = User.objects.get(pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=post)
        if form.is_valid():
            post.save()
            return redirect('/room')
    else:
        form = UserForm(instance=post)
    return render(request, 'room/edit.html', {'form': form})

def delete(request):
    data = json.loads(request.body)
    if request.method == "DELETE":
        if User.delete_by_id(data['id']):
            return HttpResponse(status=200)
    return HttpResponse(status=400)


#CREATED GROUOP


def groups(request):
    groups = Group.objects.all()
    context = {
        'groups': groups
    }
    return render(request , 'user/group.html', context)

def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = GroupForm()
        return render(request, 'lesson/create.html', {'form': form})

def edit_group(request, pk):
    post = Group.objects.get(pk=pk)
    if request.method == "POST":
        form = GroupForm(request.POST, instance=post)
        if form.is_valid():
            post.save()
            return redirect('/room')
    else:
        form = GroupForm(instance=post)
    return render(request, 'room/edit.html', {'form': form})

def delete_group(request):
    data = json.loads(request.body)
    if request.method == "DELETE":
        if Group.delete_by_id(data['id']):
            return HttpResponse(status=200)
    return HttpResponse(status=400)


def show_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    users = User.objects.filter(group = group)
    context = {
        'group': group,
        'users': users
    }
    return render(request, 'user/show_group.html', context)