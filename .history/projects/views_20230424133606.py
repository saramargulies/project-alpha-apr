from django.shortcuts import render
from projects.models import Project


def show_projects(request):
    project = Project.objects.all()
    context = {"project": accoprount}
    return render(request, "receipts/accounts.html", context)