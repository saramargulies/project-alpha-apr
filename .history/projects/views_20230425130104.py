from django.shortcuts import render, redirect
from projects.models import Project
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm


@login_required(redirect_field_name="login")
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {"projects": projects}
    return render(request, "projects/list.html", context)


@login_required(redirect_field_name="login")
def show_project(request, id):
    tasks = Task.objects.filter(project=id)
    project = Project.objects.get(id=id)
    context = {
        "tasks": tasks,
        "project": project,
    }
    return render(request, "projects/detail.html", context)


@login_required(redirect_field_name="login")
def create_receipt(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.purchaser = request.user
            project.save()
            return redirect("home")
    else:
        form = ProjectForm()
    context = {"form": form}
    return render(request, "receipts/create.html", context)
