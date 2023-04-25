from django.urls import path
from tasks.views import create_task

urlpatterns = [
    path("create/", create_task, name="list_projects"),
]
