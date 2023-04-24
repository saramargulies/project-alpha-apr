from django.shortcuts import render
from projects.models import Project


def show_projects(request):
    projects = Project.objects.all()
    context = {"project": project}
    return render(request, "list.html", context)
