from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from core.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "core/task_list.html"
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("core:task_list")
    template_name = "core/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("core:task_list")
    template_name = "core/task_form.html"


class TagsListView(generic.ListView):
    model = Tag
    template_name = "core/tags_list.html"
