from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name="login")
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {"projects": projects}
    return render(request, "projects/list.html", context)


@login_required(redirect_field_name="login")
def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        "recipe_object": recipe,
    }
    return render(request, 'recipes/detail.html', context)
