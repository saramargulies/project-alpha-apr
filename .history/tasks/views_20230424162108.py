# from django.shortcuts import render

# Create your views here.

@login_required(redirect_field_name="login")
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        "project": project,
    }
    return render(request, 'recipes/detail.html', context)
