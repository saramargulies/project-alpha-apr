from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
        related_name="tasks",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
