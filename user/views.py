import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.forms import UserForm
from .models import User
# Create your views here.
def user(request):
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
    data = json.loads(request.body.decode('utf-8'))
    if request.method == "DELETE":
        if User.delete_by_id(data['id']):
            return HttpResponse(status=200)
    return HttpResponse(status=400)



def show_user(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user/show_user.html', {'user': user})

def home(request):
    return render(request, 'base.html')