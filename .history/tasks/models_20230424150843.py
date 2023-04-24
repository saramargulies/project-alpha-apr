from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = date

    def __str__(self):
        return self.name
