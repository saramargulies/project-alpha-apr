from django.forms import ModelForm
from projects.models import Project


class TaskForm(ModelForm):
    class Meta:
        model = Project
        fields = (
            "name",
            "description",
            "owner",
        )
