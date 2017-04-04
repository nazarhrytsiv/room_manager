import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Group
from user.models import User


def validate_data_group(group):
    errors = {}
    if group['name']:
        if len(group['name']) > 30:
            errors['name'] = "Max input length is set to 30 characters."
    else:
        errors['name'] = "This field is required."
    if group['description']:
        if len(group['description']) > 620:
            errors['description'] = "Max input length is set to 620 characters."
    else:
        errors['description'] = "This field is required."
    return errors if errors else None



def groups(request):
    groups = Group.get_all()
    context = {
        'groups': groups
    }
    return render(request, 'group/group.html', context)


def create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        errors = validate_data_group(data)
        if not errors:
            group = Group(**data)
            group.save()
            return HttpResponse(status=201)
        else:
            return HttpResponse(json.dumps(errors), status=400)
    else:
        return render(request, 'group/create.html')


def edit(request, pk):
    post = Group.get_by_id(pk)
    if request.method == "PUT":
        data = json.loads(request.body)
        errors = validate_data_group(data)
        if not errors:
            group = Group(**data)
            group.save()
            return HttpResponse(status=201)
        else:
            return HttpResponse(json.dumps(errors), status=400)
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
    group = Group.get_by_id(pk)
    users = User.get_users_by_group(group)
    context = {
        'group': group,
        'users': users
    }
    return render(request, 'group/show_group.html', context)

def add_member(request, pk):
    users = User.get_users_by_group(None)
    group = Group.get_by_id(pk)
    if request.method == "POST":
        print 1111
        data = json.loads(request.body)
        user_add_to_group = User.get_by_id(data['id'])
        user_add_to_group.group = group
        user_add_to_group.save()
        return HttpResponse(status=201)
    else:
        context = {
            'users': users,
            'group': group,
        }
        return render(request, 'group/add_member.html', context)
