from django.shortcuts import render
from projects.models import Project

@login_required(re)
def list_projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/list.html", context)
