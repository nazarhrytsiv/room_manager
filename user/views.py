import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.db import IntegrityError


def validate_data_user(user):
    errors = {}
    if user['username']:
        if len(user['username']) > 30:
            errors['username'] = "Max input length is set to 30 characters."
    else:
        errors['username'] = "This field is required."
    if user['name']:
        if len(user['name']) > 30:
            errors['name'] = "Max input length is set to 50 characters."
    else:
        errors['name'] = "This field is required."
    if user['email']:
        if user['email'].find('@') == -1:
            errors['email'] = "Incorrect email. Did you forget about '@'?"
        elif len(user['email']) > 40:
            errors['email'] = "Max input length is set to 40 characters."
    else:
        errors['email'] = "This field is required."
    if user['password']:
        if len(user['password']) > 30:
            errors['password'] = "Password is too long. It should be less than 30 characters long."
        if len(user['password']) < 6:
            errors['password'] = "Password is too short. It should be more than 6 characters long."
    else:
        errors['password'] = "This field is required."

    return errors if errors else None

# Create your views here.
def users(request):
    users = User.get_all()
    context = {
        'users': users
    }
    return render(request, 'user/user.html', context)


def create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        errors = validate_data_user(data)
        if not errors:
            user = User(**data)
            try:
                user.save()
                return HttpResponse(status=201)
            except IntegrityError:
                errors = {}
                errors["username"] = "User with this username already exists."
                return HttpResponse(json.dumps(errors), status=400)
        else:
            return HttpResponse(json.dumps(errors), status=400)
    else:
        return render(request, 'user/create.html')


def edit(request, pk):
    post = User.get_by_id(pk)
    if request.method == "PUT":
        data = json.loads(request.body)
        errors = validate_data_user(data)
        if not errors:
            user = User(**data)
            #checking if we changed name
            if post.name == data["username"]:
                user.save()
                return HttpResponse(status=201)
            else:
                try:
                    user.save()
                    return HttpResponse(status=201)
                except IntegrityError:
                    errors = {}
                    errors["username"] = "User with this username already exists."
                    return HttpResponse(json.dumps(errors), status=400)
        else:
            return HttpResponse(json.dumps(errors), status=400)
    else:
        context = {
            'post': post
        }
        return render(request, 'user/edit.html', context)



def delete(request):
    data = json.loads(request.body)
    if request.method == "DELETE":
        if User.delete_by_id(data['id']):
            return HttpResponse(status=200)
    return HttpResponse(status=400)
