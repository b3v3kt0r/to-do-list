from django.urls import path

from core.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    check,
    TagsListView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("<int:pk>/check/", check, name="check"),
    path("tags/", TagsListView.as_view(), name="tags_list"),
    path("tags/create/", TagsCreateView.as_view(), name="tags_create"),
    path("tags/<int:pk>/update/", TagsUpdateView.as_view(), name="tags_update"),
    path("tags/<int:pk>/delete/", TagsDeleteView.as_view(), name="tags_delete"),
]

app_name = "core"
