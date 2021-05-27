from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(req):
    tasks = Task.objects.all()
    form = TaskForm()
    
    if req.method == "POST":
        form = TaskForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect('/todo')
    
    context = {'tasks':tasks , 'form':form}
    return render(req,'todo/index.html',context)

def deleteTask(req,pk):
    item = Task.objects.get(id=pk)
    item.delete()
    return redirect('/todo') 