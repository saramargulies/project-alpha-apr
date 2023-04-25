from django.forms import ModelForm
from tasks.models import Project


class TaskForm(ModelForm):
    class Meta:
        model = Project
        fields = (
            "name",
            "description",
            "owner",
        )
