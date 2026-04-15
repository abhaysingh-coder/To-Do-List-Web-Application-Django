from django.shortcuts import render, redirect
from .models import *
import numpy as np
import pandas as pd


# Create your views here.
def index(request):
    task=Task.objects.all()
    return render(request, 'index.html', {'task':task})

def alltask(request):
    task=Task.objects.all()
    return render(request, 'all_task.html', {'task':task})

def addtask(request):
    if request.method == 'POST':
        task = request.POST['task']
        t = Task(task=task, status='notdone')
        t.save()
        return redirect('index')
    return render(request, 'add_task.html')

def edittask(request,id):
    task=Task.objects.get(id=id)
    return render(request, 'edit_task.html', {'task':task})

def updatetask(request):
    id=request.POST['id']
    t = request.POST['task']
    Task(task=t, status='not done')
    Task.objects.filter(id=id).update(task=t)
    return redirect('index')

def changestatus(request, id):
    Task.objects.filter(id=id).update(status='done')
    return redirect('index')

def delete(request,id):
    Task.objects.get(id=id).delete()
    return redirect('alltask')
