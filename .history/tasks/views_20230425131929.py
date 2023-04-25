# from django.shortcuts import render, get_object_or_404
# from tasks.models import Task
# from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name="login")
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.purchaser = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
    context = {"form": form}
    return render(request, "projects/create.html", context)