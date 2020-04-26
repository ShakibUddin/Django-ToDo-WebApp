from django.shortcuts import render,redirect
from django.contrib import messages
from .form import userRegisterForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('/login/')
    else:
        form = userRegisterForm()
    return render(request,'users/register.html',{'form':form})

    
