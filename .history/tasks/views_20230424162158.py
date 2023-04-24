from django.shortcuts import render, get_object_or_404
from tasks.models import Task
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name="login")
def show_project(request, id):
    tasks = get_object_or_404(Task, id=id)
    context = {
        "tasks": project,
    }
    return render(request, 'recipes/detail.html', context)
