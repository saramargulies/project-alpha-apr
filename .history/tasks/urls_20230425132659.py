from django.urls import path
from tasks.views import create_task

urlpatterns = [
    path("create/", list_projects, name="list_projects"),
]
