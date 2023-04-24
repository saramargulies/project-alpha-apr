from django.shortcuts import render, get_object_or_404
from tasks.models import Task
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name="login")
def show_project(request, id):
    project = get_object_or_404(Task, id=id)
    context = {
        "project": project,
    }
    return render(request, 'recipes/detail.html', context)
