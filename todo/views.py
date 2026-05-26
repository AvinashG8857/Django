from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def task_list(request):
    tasks= Task.objects.filter(user=request.user)
    return render(request,'task_list.html',{'tasks':tasks})

@login_required
def add_task(request):
    if request.method=='POST':
        title= request.POST.get("title")
        due_date= request.POST.get("due_date")
        Task.objects.create(
            user= request.user,
            title= title,
            due_date= due_date
        )

        return redirect('task_list')
    return render(request,'add_task.html')

def register(request):
    form= UserCreationForm()
    if request.method=="POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,"register.html",{'form':form})

def update_task(request):
    pass
