from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import ToDoItem
from datetime import datetime

def home(request):
    return render(request,'todo/home.html')

@login_required
def mytask(request):
    username = request.user.username
    my_to_do_items = ToDoItem.objects.all()
    data={
    'todos': my_to_do_items,
    'name' : username,
    }
    return render(request,'todo/mytask.html',data)

def addtask(request):
    username = request.user.username
    added_on = datetime.today().strftime('%Y-%m-%d')
    newtask = ToDoItem(name=username,task=request.POST.get('task'),addedon=added_on,duedate=request.POST.get('date'))
    newtask.save()
    return HttpResponseRedirect('/mytask/')

def about(request):
    return render(request,'todo/about.html')

def contact(request):
    return render(request,'todo/contact.html')

def deletetask(request,todo_id):
    task_to_delete = ToDoItem.objects.get(id=todo_id)
    task_to_delete.delete()
    return HttpResponseRedirect('/mytask/')

# Create your views here.
