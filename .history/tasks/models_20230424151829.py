from django.db import models
from django.conf import settings


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    project = models.ForeignKey(
        "Project"
        related_name="tasks",
        on_delete=models.CASCADE,
        null=True
    )

    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="tasks",
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name
