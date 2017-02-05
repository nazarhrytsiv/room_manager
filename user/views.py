import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.forms import UserForm
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