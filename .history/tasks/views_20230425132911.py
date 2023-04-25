from django.shortcuts import render, redirect
from tasks.forms import TaskForm
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name="login")
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(False)
            return redirect("list_projects")
    else:
        form = TaskForm()
    context = {"form": form}
    return render(request, "tasks/create.html", context)
