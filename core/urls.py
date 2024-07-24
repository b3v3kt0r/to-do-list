from django.urls import path

from core.views import TaskListView

urlpatterns = [
    path("", TaskListView, name="task_list"),
]

app_name = "core"
