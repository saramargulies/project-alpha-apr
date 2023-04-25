from django.urls import path
from tasks.views import create_task

urlpatterns = [
    path("", list_projects, name="list_projects"),
]
