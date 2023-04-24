from django.db import models
from django.conf import settings

class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="tasks",
        on_delete=
    )

    def __str__(self):
        return self.name
