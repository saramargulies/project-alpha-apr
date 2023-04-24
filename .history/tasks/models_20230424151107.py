from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    due_date = models.DateField()
    is_completed = models.BooleanField()

    def __str__(self):
        return self.name
