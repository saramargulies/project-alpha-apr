from django.shortcuts import render, redirect
from tasks.forms import TaskForm
from tasks.models import Task
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name="login")
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
    context = {"form": form}
    return render(request, "tasks/create.html", context)


@login_required(redirect_field_name="login")
def show_my_tasks(request,):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "tasks": tasks,
    }
    return render(request, "tasks/detail.html", context)
