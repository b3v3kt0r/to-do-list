from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import generic

from core.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "core/task_list.html"
    queryset = Task.objects.prefetch_related("tags")


class TagsListView(generic.ListView):
    model = Tag
    template_name = "core/tags_list.html"
