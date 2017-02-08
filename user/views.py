import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from user.forms import UserForm
from .models import User



# Create your views here.
def users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'user/user.html', context)


def create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user')
        else:
            return HttpResponse(status=400)
    else:
        form = UserForm()
        return render(request, 'user/create.html', {'form': form})


def edit(request, pk):
    post = User.objects.get(pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=post)
        if form.is_valid():
            post.save()
            return redirect('/user')
    else:
        form = UserForm(instance=post)
    return render(request, 'user/edit.html', {'form': form})


def delete(request):
    data = json.loads(request.body)
    if request.method == "DELETE":
        if User.delete_by_id(data['id']):
            return HttpResponse(status=200)
    return HttpResponse(status=400)

