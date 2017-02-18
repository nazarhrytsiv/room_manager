import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User


# Create your views here.
def users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'user/user.html', context)


def create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = User(**data)
        user.save()
        return HttpResponse(status=201)
    else:
        return render(request, 'user/create.html')


def edit(request, pk):
    post = User.get(pk=pk)
    if request.method == "POST":
        data = {}
        result = request.body.split('&')
        for i in result:
            data.update(dict([i.split("="), ]))
        user = User(username=data['username'], name=data['name'], email=data['email'], password=data['password'], )
        user.id = pk
        user.save()
        return redirect('/user')
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
