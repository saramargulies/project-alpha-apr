from django.shortcuts import render, get_object_or_404
from projects.models import Project
from tasks.models import Task
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name="login")
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {"projects": projects}
    return render(request, "projects/list.html", context)


@login_required(redirect_field_name="login")
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    project = get_object_or_404(Project, id=id)
    context = {
        "project": project,
    }
    return render(request, "projects/detail.html", context)
