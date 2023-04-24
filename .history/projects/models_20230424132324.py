from django.db import models
from django


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )