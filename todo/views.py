from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoItem

def home(request):
    return render(request,'todo/home.html')

def mytask(request):
    my_to_do_items = ToDoItem.objects.all()
    return render(request,'todo/mytask.html',
        {
        'todos':my_to_do_items,
        })
        
def addtask(request):
    newtask = ToDoItem(task=request.POST.get('task'),date=request.POST.get('date'))
    newtask.save()
    return HttpResponseRedirect('/mytask/')

def about(request):
    return render(request,'todo/about.html')

def contact(request):
    return render(request,'todo/contact.html')

def deletetask(request,todo_id):
    print(f"Id passed {todo_id}")
    task_to_delete = ToDoItem.objects.get(id=todo_id)
    task_to_delete.delete()
    return HttpResponseRedirect('/mytask/')

# Create your views here.
