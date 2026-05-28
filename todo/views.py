from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib.auth import logout


# ✅ Task List
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-due_date')
    return render(request, 'task_list.html', {'tasks': tasks})


# ✅ Add Task
@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        due_date = request.POST.get("due_date")

        if title and due_date:
            Task.objects.create(
                user=request.user,
                title=title,
                due_date=due_date
            )
            return redirect('task_list')

    return render(request, 'add_task.html')


# ✅ Register (AUTO LOGIN AFTER REGISTER 🚀)
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)   # ✅ Auto login after register
            return redirect('task_list')

    return render(request, "register.html", {'form': form})


# ✅ Update Task (SECURE)
@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)

    if request.method == "POST":
        task.title = request.POST.get('title')
        task.due_date = request.POST.get("due_date")
        task.completed = request.POST.get("completed") == 'on'
        task.save()

        return redirect('task_list')

    return render(request, 'update_task.html', {'task': task})


# ✅ Delete Task (SECURE)
@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk, user=request.user)

    if request.method == "POST":   # ✅ Only allow POST delete
        task.delete()

    return redirect('task_list')


def user_logout(request):
    logout(request)
    return redirect('login')

