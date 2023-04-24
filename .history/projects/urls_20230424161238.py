from django.urls import path
from projects.views import (list_projects, )

urlpatterns = [
    path("", list_projects, name="list_projects"),
    path("<int:id>/", list_projects, name="list_projects"),
]
