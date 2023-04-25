from django.forms import ModelForm
from projects.models import Project
from django.shortcuts import redirect


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = (
            "name",
            "description",
        )
