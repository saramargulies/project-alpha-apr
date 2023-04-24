from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    

    def __str__(self):
        return self.name
