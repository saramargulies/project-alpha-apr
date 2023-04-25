from django.shortcuts import render, redirect
from tasks.forms import TaskForm
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
def show_project(request, id):
    tasks = Task.objects.filter(project=id)
    project = Project.objects.get(id=id)
    context = {
        "tasks": tasks,
        "project": project,
    }
    return render(request, "projects/detail.html", context)

